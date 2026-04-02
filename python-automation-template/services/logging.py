# services/logger.py
import logging
import os
import sys
from datetime import datetime


class LoggerService:
    def __init__(self, log_level, log_dir):
        # Create log directory if needed
        os.makedirs(log_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(log_dir, f"logs_{timestamp}.log")

        # Convert string to logging level
        level = getattr(logging, log_level.upper(), logging.INFO)

        # Create logger
        self.logger = logging.getLogger("Automation")
        self.logger.setLevel(level)
        self.logger.handlers.clear()  # Remove existing handlers

        class ColorFormatter(logging.Formatter):
            COLORS = {
                logging.DEBUG: "\033[96m",  # Cyan
                logging.INFO: "\033[92m",  # Green
                logging.WARNING: "\033[93m",  # Yellow
                logging.ERROR: "\033[91m",  # Red
                logging.CRITICAL: "\033[1;91m",  # Bold Red
            }
            RESET = "\033[0m"

            def format(self, record):
                color = self.COLORS.get(record.levelno, self.RESET)
                message = super().format(record)
                return f"{color}{message}{self.RESET}"

        # Console handler (with color)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(
            ColorFormatter("%(asctime)s | %(levelname)s | %(message)s")
        )
        self.logger.addHandler(console_handler)

        # File handler (no color)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        )
        self.logger.addHandler(file_handler)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
