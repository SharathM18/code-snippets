import tomllib
from pathlib import Path


def load_config(config_path: Path, env: str) -> dict:
    """Load configuration from TOML file"""

    with open(config_path, "rb") as f:
        full_config = tomllib.load(f)  # Dict output

    # Start with default config
    config = full_config.get("default", {}).copy()

    # Override with environment config
    env_config = full_config.get(env, {})
    config.update(env_config)  # default + env specific config

    # Add environment name to config
    config["environment"] = env

    return config
