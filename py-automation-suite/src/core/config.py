from pathlib import Path

import yaml


def load_config(config_file: Path, script_name: str = "default") -> dict:
    if not config_file.is_file():
        raise FileNotFoundError(
            f"Config file not found or is not a file: {config_file}"
        )
    with open(config_file) as f:
        raw_config = yaml.safe_load(f) or {}

    default_config = raw_config.get("default", {})
    script_config = raw_config.get(script_name, {})
    full_config = {**default_config, **script_config}

    return full_config
