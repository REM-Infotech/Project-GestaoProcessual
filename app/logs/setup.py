# Initialize Logging
import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path


def initialize_logging(
    log_file="app.log", log_level=logging.DEBUG, max_bytes=1024 * 1024, backup_count=1
):
    """
    Initializes a logger with a rotating file handler and a console handler.

    Args:
        log_file (str): Path to the log file.
        log_level (int): Logging level (e.g., logging.DEBUG).
        max_bytes (int): Maximum size of the log file before rotating (in Mbytes).
        backup_count (int): Number of backup files to keep.

    Returns:
        logger: Configured logger instance.
    """

    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # File handler
    file_handler = RotatingFileHandler(
        os.path.join(Path(__file__).parent.resolve(), log_file),
        maxBytes=max_bytes,
        backupCount=backup_count,
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
