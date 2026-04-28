import json
import os
import subprocess
import tempfile
import uuid
from collections.abc import Generator
from contextlib import contextmanager
from pathlib import Path

import pendulum
import yaml
from loguru import logger


def get_uuid() -> str:
    return str(uuid.uuid4())


def get_timestamp() -> str:
    return pendulum.now().format("YYYYMMDD_HHmmss")


def get_unique_filename(extension: str, *file_name: str) -> str:
    try:
        clean_extension = extension if extension.startswith(".") else f".{extension}"
        prefix = "_".join(file_name) if file_name else "file"

        return f"{prefix}_{get_timestamp()}{clean_extension}"
    except Exception as e:
        logger.error(f"Failed to generate filename: {e}")
        return ""


def run_sys_cmd(cmd: list[str], extra_env: dict | None = None) -> str:
    try:
        # Get a safe copy of current variables
        child_env = os.environ.copy()

        if extra_env:
            child_env.update(extra_env)

        logger.info(f"Executing command: {' '.join(cmd)}")

        out = subprocess.run(
            cmd, env=child_env, shell=False, text=True, capture_output=True, check=True
        )

        return out.stdout.strip()

    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed with code {e.returncode}: {' '.join(cmd)}")
        if e.stderr:
            logger.error(f"stderr: {e.stderr.strip()}")
    except Exception as e:
        logger.error(f"Unexpected error running command: {e}")

    return ""


@contextmanager
def get_temp_dir() -> Generator[Path, None, None]:
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield Path(tmp_dir)


def read_json(json_file: Path) -> dict:
    try:
        return json.loads(json_file.read_text(encoding="utf-8"))
    except Exception as e:
        logger.error(f"Failed to read JSON {json_file}: {e}")
        return {}


def write_json(json_file: Path, data: dict, indent: int = 2) -> None:
    try:
        json_file.write_text(
            json.dumps(data, indent=indent, ensure_ascii=False), encoding="utf-8"
        )
    except Exception as e:
        logger.error(f"Failed to write JSON {json_file}: {e}")


def read_yaml(yaml_file: Path) -> dict:
    try:
        with open(yaml_file) as f:
            return yaml.safe_load(f) or {}
    except Exception as e:
        logger.error(f"Failed to read YAML {yaml_file}: {e}")
        return {}
