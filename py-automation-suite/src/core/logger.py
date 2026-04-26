import sys
from pathlib import Path

import pendulum
from loguru import logger


def setup_logging(log_dir: Path, log_level: str = "INFO"):
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

    # log file
    timestamp = pendulum.now().format("YYYYMMDD_HHmmss")
    log_file = log_dir / f"logs_{timestamp}.log"
    logger.add(
        log_file,
        level=log_level.upper(),
        format="{time:YYYY-MM-DD HH:mm:ss} | {level:<8} | {name}:{function}:{line} | {message}",
        encoding="utf-8",
        enqueue=True,
        # rotation="10 MB",
        # retention="7 days",
    )
