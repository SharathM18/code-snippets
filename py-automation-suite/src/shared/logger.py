import sys
from pathlib import Path

import pendulum
from loguru import logger


def setup_logging(log_dir: Path, log_level: str):

    # Remove default handler
    logger.remove()

    log_dir.mkdir(parents=True, exist_ok=True)

    # console logs
    logger.add(
        sys.stdout,
        level=log_level.upper(),
        colorize=True,
        # format="{time:time:YYYY-MM-DD HH:mm:ss} | {level} | {message} | {extra}",
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level:<8}</level> | "
            "<cyan>{name}</cyan> - <level>{message}</level>"
        ),
    )

    # log file format
    timestamp = pendulum.now().format("YYYYMMDD_HHmmss")
    log_file = log_dir / f"logs_{timestamp}.log"
    logger.add(
        log_file,
        level=log_level.upper(),
        # format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message} | {extra}",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level:<8} | {name}:{function}:{line} | {message}",
        encoding="utf-8",
        enqueue=True,
    )


"""
## Logging Levels Reference

| Level     | Method             | Description                          |
|----------|---------------------|--------------------------------------|
| TRACE    | `logger.trace()`    | Very fine-grained debugging details  |
| DEBUG    | `logger.debug()`    | Debugging information                |
| INFO     | `logger.info()`     | General operational messages         |
| SUCCESS  | `logger.success()`  | Successful operations (non-standard) |
| WARNING  | `logger.warning()`  | Something unexpected but recoverable |
| ERROR    | `logger.error()`    | Errors that need attention           |
| CRITICAL | `logger.critical()` | Severe failures, system may stop     |

from loguru import logger

## Basic usage with different log levels
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.success("This is a success message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
"""
