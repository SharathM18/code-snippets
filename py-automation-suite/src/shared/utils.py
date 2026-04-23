import os
import subprocess
import tempfile
from pathlib import Path

import pendulum
from loguru import logger


def generate_unique_filename(extension: str, prefix: str = "", env: str = ""):
    """
    Example output: dev_report_20260422_143022.csv
    """
    try:
        timestamp = pendulum.now().format("YYYYMMDD_HHmmss")
        env_str = f"{env}_" if env else ""
        clean_ext = extension if extension.startswith(".") else f".{extension}"
        return f"{env_str}{prefix}_{timestamp}_{clean_ext}"
    except Exception as e:
        logger.error(f"Failed to generate filename: {e}")
        return ""


def run_sys_cmd(cmd: list):
    try:
        # Get a safe copy of current variables
        child_env = os.environ.copy()

        # Inject any script-specific `export` variable here
        # child_env["ENV"] = "dev"

        logger.info(f"Executing command: {cmd}")

        shell_output = subprocess.run(
            cmd, env=child_env, shell=True, text=True, capture_output=True, check=True
        )
        return shell_output.stdout.strip()

    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed: {cmd} | Error: {e.stderr.strip()}")
        return ""


def get_safe_temp_dir():
    """
    This creates a safe, unique folder (e.g., /tmp/tmp_8x2a9d/)
    It automatically cleans itself up when the "with" block ends
    """
    try:
        temp_dir_obj = tempfile.TemporaryDirectory()
        temp_path = Path(temp_dir_obj.name)
        return temp_dir_obj, temp_path
    except Exception as e:
        logger.error(f"Failed to create temporary directory: {e}")
        return "", ""
