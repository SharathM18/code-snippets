```bash
python cli.py script-one \
  --env dev \
  --path /home/msharathh/data.csv \
  --paths /home/msharathh/data1.csv /home/msharathh/data2.csv \
  --dir /home/msharathh/ \
  --dirs /home/msharathh/type1 /home/msharathh/type2 \
  --boolean-value True \
  --number-value 12 \
  --log-level DEBUG
```

Set Up a Virtual Environment
Install the Package

```bash
pip install -e .                            # Install with only runtime dependencies
pip install -e ".[dev]"                     # Install with development tools
pip install -e ".[dev,js]"
pip install -e ".[all]"                     # Install everything at once

# Check if the command is found
which automate          # Linux/macOS
where automate          # Windows


automate --help                             # Show help

# Run a Script
automate --env dev script-one ./data/input/sample.html
```
