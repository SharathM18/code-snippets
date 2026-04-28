# Automation scripts suite

## Setup

```bash
uv sync --no-dev                               # Automatically crates .venv and install core deps
uv pip install -e .                            # Install core only + registers CLI cmd

uv run automate --help                         # top level help
uv run automate script1 --help                 # script1 specific help

# Run a Script
uv run automate script1 \
  --path ./settings.yaml \
  --paths ./settings.yaml \
  --paths ./pyproject.toml \
  --out-dir ./output \
  --log-level INFO \
  --number-value 5 \
  --boolean-value

uv run automate script2 \
  --out-dir ./output \
  --log-level INFO \
  --number-value 5
```

# Development commands fro Lint

```
chmod +x lint.sh
uv run bash lint.sh
```
