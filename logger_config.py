import logging
from logging.handlers import RotatingFileHandler
from typing import Optional


def setup_logger(log_file: str = "posture_guard.log", level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns a logger that prints to the console and writes to a rotating log file.

    :param log_file: File name/path where log messages should be written.
    :param level: The threshold logging level.
    :return: Configured logging.Logger instance.
    """
    logger = logging.getLogger("PostureGuard")
    logger.setLevel(level)

    # Avoid adding duplicate handlers if the logger has already been setup
    if logger.handlers:
        return logger

    # Format config
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')

    # Console output handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Rotating file handler
    try:
        file_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=3, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except OSError:
        logger.warning("Could not initialize file logging handler. Logging only to standard console output.")

    return logger
