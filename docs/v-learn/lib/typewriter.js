/**
 * Typewriter effect for code blocks in reveal.js slides.
 *
 * Usage:
 *   <pre class="typewriter-code" data-speed="30"><code class="language-python">
 *     ... your code ...
 *   </code></pre>
 *
 *   Include this script after reveal.js initialization.
 *
 * Options (data attributes on <pre>):
 *   data-speed   — ms per character (default: 25)
 *   data-delay   — ms before starting (default: 300)
 *   data-cursor   — show blinking cursor (default: true)
 *
 * The code is syntax-highlighted first by reveal.js/highlight.js,
 * then the VISIBLE TEXT is typed character by character while
 * preserving the HTML structure (colors, spans, etc.).
 */

(function () {
  'use strict';

  const DEFAULTS = { speed: 25, delay: 300, cursor: true };

  // Store original highlighted HTML for each block
  const originals = new Map();

  /**
   * Type out the innerHTML of a <code> element character by character,
   * preserving syntax highlighting spans.
   */
  function typewrite(codeEl, opts) {
    const html = originals.get(codeEl);
    if (!html) return;

    // Parse the full highlighted HTML into a flat list of:
    // { type: 'tag'|'char', value: string }
    const tokens = [];
    let i = 0;
    while (i < html.length) {
      if (html[i] === '<') {
        // Consume entire tag
        const end = html.indexOf('>', i);
        tokens.push({ type: 'tag', value: html.slice(i, end + 1) });
        i = end + 1;
      } else if (html[i] === '&') {
        // HTML entity — treat as single visible char
        const end = html.indexOf(';', i);
        if (end !== -1 && end - i < 10) {
          tokens.push({ type: 'char', value: html.slice(i, end + 1) });
          i = end + 1;
        } else {
          tokens.push({ type: 'char', value: html[i] });
          i++;
        }
      } else {
        tokens.push({ type: 'char', value: html[i] });
        i++;
      }
    }

    // Clear content, add cursor
    codeEl.innerHTML = '';
    let cursorEl = null;
    if (opts.cursor) {
      cursorEl = document.createElement('span');
      cursorEl.className = 'tw-cursor';
      cursorEl.textContent = '\u258C'; // ▌ block cursor
      codeEl.appendChild(cursorEl);
    }

    let tokenIdx = 0;
    let buffer = '';

    function tick() {
      if (tokenIdx >= tokens.length) {
        // Done — remove cursor after a beat
        if (cursorEl) {
          setTimeout(() => cursorEl.classList.add('tw-cursor-idle'), 500);
        }
        return;
      }

      const token = tokens[tokenIdx++];
      buffer += token.value;

      if (token.type === 'tag') {
        // Tags are added instantly (not visible), continue to next
        tick();
        return;
      }

      // Visible character — update display
      if (cursorEl) {
        codeEl.innerHTML = buffer;
        codeEl.appendChild(cursorEl);
      } else {
        codeEl.innerHTML = buffer;
      }

      // Vary speed slightly for natural feel
      let charDelay = opts.speed;
      if (token.value === '\n') charDelay = opts.speed * 3; // pause on newlines
      else if (token.value === ' ') charDelay = opts.speed * 0.5;
      else charDelay += (Math.random() - 0.5) * opts.speed * 0.4;

      setTimeout(tick, Math.max(5, charDelay));
    }

    setTimeout(tick, opts.delay);
  }

  /**
   * Initialize: capture original HTML after highlight.js runs,
   * then set up slide-change triggers.
   */
  function init() {
    // Wait a frame for highlight.js to finish
    requestAnimationFrame(() => {
      document.querySelectorAll('pre.typewriter-code code').forEach(code => {
        // Store the highlighted HTML
        originals.set(code, code.innerHTML);
        // Initially hide content (will type on slide entry)
        code.innerHTML = '';
      });
    });

    // On slide change, trigger typewriter for blocks in the new slide
    Reveal.on('slidechanged', event => {
      event.currentSlide.querySelectorAll('pre.typewriter-code code').forEach(code => {
        const pre = code.closest('pre');
        const opts = {
          speed: parseInt(pre.dataset.speed) || DEFAULTS.speed,
          delay: parseInt(pre.dataset.delay) || DEFAULTS.delay,
          cursor: pre.dataset.cursor !== 'false'
        };
        // Reset and replay
        code.innerHTML = '';
        typewrite(code, opts);
      });
    });

    // Also handle initial slide
    Reveal.on('ready', event => {
      event.currentSlide.querySelectorAll('pre.typewriter-code code').forEach(code => {
        const pre = code.closest('pre');
        const opts = {
          speed: parseInt(pre.dataset.speed) || DEFAULTS.speed,
          delay: parseInt(pre.dataset.delay) || DEFAULTS.delay,
          cursor: pre.dataset.cursor !== 'false'
        };
        typewrite(code, opts);
      });
    });
  }

  // CSS for the cursor
  const style = document.createElement('style');
  style.textContent = `
    .tw-cursor {
      color: #00d2ff;
      animation: tw-blink 0.7s step-end infinite;
      font-weight: normal;
      margin-left: -2px;
    }
    .tw-cursor-idle {
      animation: tw-blink 1.2s step-end infinite;
      opacity: 0.5;
    }
    @keyframes tw-blink {
      50% { opacity: 0; }
    }
    /* Ensure code block has min-height to prevent layout shift */
    pre.typewriter-code code {
      min-height: 2em;
      display: block;
    }
  `;
  document.head.appendChild(style);

  // Skip typewriter in print-pdf mode — show all code statically
  if (/print-pdf/i.test(window.location.search)) return;

  // Initialize after Reveal is ready
  if (typeof Reveal !== 'undefined') {
    if (Reveal.isReady && Reveal.isReady()) {
      init();
    } else {
      Reveal.on('ready', init);
    }
  } else {
    document.addEventListener('DOMContentLoaded', () => {
      if (typeof Reveal !== 'undefined') init();
    });
  }
})();
