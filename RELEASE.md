# Releasing PyXFlow to PyPI

## Prerequisites

```bash
pip install build twine
```

## Steps

### 1. Bump version

Update version in **both** files (must match):

- `pyproject.toml` -- `version = "X.Y.Z"`
- `src/pyxflow/__init__.py` -- `__version__ = "X.Y.Z"`

### 2. Switch README images to absolute URLs

PyPI cannot resolve relative paths. Temporarily replace all image `src` attributes:

```
src="docs/  -->  src="https://manolo.github.io/pyxflow/
```

The repo keeps relative paths (work on GitHub without camo proxy). The absolute URLs use GitHub Pages which has no size limit and works with PyPI's camo proxy.

**Quick sed:**
```bash
sed -i '' 's|src="docs/|src="https://manolo.github.io/pyxflow/|g' README.md
```

### 3. Build

```bash
rm -rf dist/ build/
python -m build
```

This creates both `pyxflow-X.Y.Z-py3-none-any.whl` (~6.6 MB) and `pyxflow-X.Y.Z.tar.gz` (~6.6 MB).

The sdist only includes `src/`, `README.md`, `LICENSE`, and `pyproject.toml` (configured in `pyproject.toml` `[tool.hatch.build.targets.sdist]`).

### 4. Upload

```bash
twine upload dist/*
```

Requires PyPI credentials (configured via `~/.pypirc` or environment variables).

### 5. Restore relative paths and commit

```bash
sed -i '' 's|src="https://manolo.github.io/pyxflow/|src="docs/|g' README.md
git add README.md pyproject.toml src/pyxflow/__init__.py
git commit -m "Bump to X.Y.Z"
git push
```

### 6. Verify

- PyPI: https://pypi.org/project/pyxflow/
- Install: `pip install pyxflow==X.Y.Z`

## Image hosting summary

| Site | Image format | Why |
|------|-------------|-----|
| GitHub repo | `src="docs/screenshots/..."` | Relative paths resolve from repo root, no camo proxy, no size limit |
| PyPI | `src="https://manolo.github.io/pyxflow/screenshots/..."` | Absolute URLs via GitHub Pages, works with PyPI camo proxy |

## Notes

- PyPI does not allow re-uploading the same version. If you need to fix something, bump the patch version.
- The Vaadin frontend bundle is included in the wheel at `pyxflow/bundle/`. It is ~6 MB compressed.
- GIFs larger than ~10 MB break on GitHub's camo proxy. The compressed versions in `docs/screenshots/` are under this limit.
