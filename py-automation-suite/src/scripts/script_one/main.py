from pathlib import Path

from loguru import logger
from src.shared.logger import setup_logging

# GLOBAL CONSTANTS
SCRIPT_ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_ROOT / "outs"
LOG_DIR = OUTPUT_DIR / "logs"
DATA_DIR = OUTPUT_DIR / "data"


def run(config: dict, cli_args: dict):
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    setup_logging(log_dir=LOG_DIR, log_level=config["log_lvl"])

    logger.info("loggerfilesetup")
    print("logger files setup")
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.success("This is a success message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    logger.info("Automation completed successfully")
