/**
 * PyXFlow MCP Server - Cloudflare Worker
 *
 * Stateless MCP Streamable HTTP server. Fetches pre-generated docs
 * from GitHub Pages and serves them via 6 MCP tools.
 *
 * Architecture:
 *   Claude/AI --POST /mcp--> This Worker --fetch()--> GitHub Pages CDN
 */

const BASE_URL = "https://manolo.github.io/pyxflow/mcp";
const SERVER_NAME = "pyxflow";
const SERVER_VERSION = "1.0.0";
const PROTOCOL_VERSION = "2025-03-26";

// ---------------------------------------------------------------------------
//  Types
// ---------------------------------------------------------------------------

interface JsonRpcRequest {
  jsonrpc: "2.0";
  id?: string | number;
  method: string;
  params?: Record<string, unknown>;
}

interface JsonRpcResponse {
  jsonrpc: "2.0";
  id: string | number | null;
  result?: unknown;
  error?: { code: number; message: string; data?: unknown };
}

// ---------------------------------------------------------------------------
//  Content fetching with Cloudflare cache
// ---------------------------------------------------------------------------

async function fetchContent(path: string): Promise<string> {
  const url = `${BASE_URL}/${path}`;
  const response = await fetch(url, {
    cf: { cacheTtl: 3600, cacheEverything: true },
  } as RequestInit);
  if (!response.ok) {
    throw new Error(`Not found: ${path}`);
  }
  return response.text();
}

function normalizeComponentName(name: string): string {
  if (name.includes("-")) return name.toLowerCase();
  return name.replace(/([a-z0-9])([A-Z])/g, "$1-$2").toLowerCase();
}

function normalizeName(name: string): string {
  return name.toLowerCase().replace(/[_ ]/g, "-");
}

// ---------------------------------------------------------------------------
//  Tool definitions
// ---------------------------------------------------------------------------

const TOOLS = [
  {
    name: "get_pyxflow_primer",
    description:
      "Get the PyXFlow overview, quick start guide, architecture, import patterns, and component categories. Call this FIRST before writing any PyXFlow code.",
    inputSchema: { type: "object" as const, properties: {} },
  },
  {
    name: "list_components",
    description:
      "List all available PyXFlow components with their category and description.",
    inputSchema: { type: "object" as const, properties: {} },
  },
  {
    name: "get_component_api",
    description:
      "Get the full API documentation for a specific PyXFlow component: constructor, methods, properties, theme variants, and related classes.",
    inputSchema: {
      type: "object" as const,
      properties: {
        component_name: {
          type: "string",
          description:
            'Component name in any format: "TextField", "text-field", "Grid", etc.',
        },
      },
      required: ["component_name"],
    },
  },
  {
    name: "get_example",
    description:
      'Get a complete runnable PyXFlow example view. Available: "hello", "grid", "crud", "master-detail", "push", "dialog", "app-layout".',
    inputSchema: {
      type: "object" as const,
      properties: {
        example_name: {
          type: "string",
          description:
            'Example name: "hello", "grid", "crud", "master-detail", "push", "dialog", "app-layout".',
        },
      },
      required: ["example_name"],
    },
  },
  {
    name: "get_pattern",
    description:
      'Get a cross-cutting pattern guide with code examples. Available: "routing", "binder", "data-provider", "push", "renderers", "app-layout", "field-validation", "client-callable", "theming", "project-setup".',
    inputSchema: {
      type: "object" as const,
      properties: {
        pattern_name: {
          type: "string",
          description:
            'Pattern name: "routing", "binder", "data-provider", "push", "renderers", "app-layout", "field-validation", "client-callable", "theming", "project-setup".',
        },
      },
      required: ["pattern_name"],
    },
  },
  {
    name: "get_constants",
    description:
      'Get enum constants and their values. Categories: "all", "layout", "grid", "field", "variants". Default: "all".',
    inputSchema: {
      type: "object" as const,
      properties: {
        category: {
          type: "string",
          description:
            'Category: "all", "layout", "grid", "field", "variants". Default: "all".',
        },
      },
    },
  },
];

// ---------------------------------------------------------------------------
//  Tool execution
// ---------------------------------------------------------------------------

async function executeTool(
  name: string,
  args: Record<string, unknown>
): Promise<{ content: Array<{ type: "text"; text: string }> }> {
  let text: string;

  switch (name) {
    case "get_pyxflow_primer":
      text = await fetchContent("primer.md");
      break;

    case "list_components":
      text = await fetchContent("components.json");
      break;

    case "get_component_api": {
      const componentName = normalizeComponentName(
        (args.component_name as string) || ""
      );
      text = await fetchContent(`components/${componentName}.md`);
      break;
    }

    case "get_example": {
      const exampleName = normalizeName((args.example_name as string) || "");
      text = await fetchContent(`examples/${exampleName}.md`);
      break;
    }

    case "get_pattern": {
      const patternName = normalizeName((args.pattern_name as string) || "");
      text = await fetchContent(`patterns/${patternName}.md`);
      break;
    }

    case "get_constants": {
      const category = normalizeName((args.category as string) || "all");
      text = await fetchContent(`constants/${category}.md`);
      break;
    }

    default:
      throw new Error(`Unknown tool: ${name}`);
  }

  return { content: [{ type: "text", text }] };
}

// ---------------------------------------------------------------------------
//  JSON-RPC handler
// ---------------------------------------------------------------------------

function jsonRpcResponse(
  id: string | number | null,
  result: unknown
): JsonRpcResponse {
  return { jsonrpc: "2.0", id, result };
}

function jsonRpcError(
  id: string | number | null,
  code: number,
  message: string
): JsonRpcResponse {
  return { jsonrpc: "2.0", id, error: { code, message } };
}

async function handleRpc(req: JsonRpcRequest): Promise<JsonRpcResponse | null> {
  const { method, params, id } = req;

  switch (method) {
    case "initialize":
      return jsonRpcResponse(id ?? null, {
        protocolVersion: PROTOCOL_VERSION,
        capabilities: { tools: {} },
        serverInfo: { name: SERVER_NAME, version: SERVER_VERSION },
      });

    case "notifications/initialized":
      // Notification, no response needed
      return null;

    case "tools/list":
      return jsonRpcResponse(id ?? null, { tools: TOOLS });

    case "tools/call": {
      const toolName = (params?.name as string) || "";
      const toolArgs = (params?.arguments as Record<string, unknown>) || {};
      try {
        const result = await executeTool(toolName, toolArgs);
        return jsonRpcResponse(id ?? null, result);
      } catch (e) {
        const message = e instanceof Error ? e.message : String(e);
        return jsonRpcResponse(id ?? null, {
          content: [{ type: "text", text: `Error: ${message}` }],
          isError: true,
        });
      }
    }

    case "ping":
      return jsonRpcResponse(id ?? null, {});

    default:
      return jsonRpcError(id ?? null, -32601, `Method not found: ${method}`);
  }
}

// ---------------------------------------------------------------------------
//  HTTP handler
// ---------------------------------------------------------------------------

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, mcp-session-id",
  "Access-Control-Expose-Headers": "mcp-session-id",
};

export default {
  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);

    // CORS preflight
    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: CORS_HEADERS });
    }

    // Health check
    if (url.pathname === "/mcp" && request.method === "GET") {
      return new Response(
        JSON.stringify({
          name: SERVER_NAME,
          version: SERVER_VERSION,
          protocol: "mcp",
          transport: "streamable-http",
        }),
        {
          headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
        }
      );
    }

    // MCP endpoint
    if (url.pathname === "/mcp" && request.method === "POST") {
      let body: unknown;
      try {
        body = await request.json();
      } catch {
        return new Response(
          JSON.stringify(jsonRpcError(null, -32700, "Parse error")),
          {
            status: 400,
            headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
          }
        );
      }

      // Handle batch or single request
      const isBatch = Array.isArray(body);
      const requests: JsonRpcRequest[] = isBatch
        ? (body as JsonRpcRequest[])
        : [body as JsonRpcRequest];

      const responses: JsonRpcResponse[] = [];
      for (const req of requests) {
        const resp = await handleRpc(req);
        if (resp !== null) {
          responses.push(resp);
        }
      }

      if (responses.length === 0) {
        return new Response(null, {
          status: 204,
          headers: CORS_HEADERS,
        });
      }

      const result = isBatch ? responses : responses[0];
      return new Response(JSON.stringify(result), {
        headers: {
          ...CORS_HEADERS,
          "Content-Type": "application/json",
        },
      });
    }

    return new Response("Not Found", { status: 404, headers: CORS_HEADERS });
  },
};
