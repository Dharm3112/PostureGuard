import logging
from logging.handlers import RotatingFileHandler
from typing import Optional


def setup_logger(log_file: str = "posture_guard.log", level: int = logging.INFO, log_format: Optional[str] = None, encoding: str = "utf-8") -> logging.Logger:  # Setup centralized logger instance with default parameters
    """
    Configures and returns a logger that prints to the console and writes to a rotating log file.

    :param log_file: File name/path where log messages should be written.
    :param level: The threshold logging level.
    :return: Configured logging.Logger instance.
    """
    # Retrieve or register centralized application logger instance
    logger = logging.getLogger("PostureGuard")
    # Set minimum severity event logging threshold filter level
    logger.setLevel(level)

    # Avoid adding duplicate handlers if the logger has already been setup
    # Check if any logging handlers have already been configured
    if logger.handlers:
        # Verify if an explicit format string is provided
        if log_format:
            # Compile new formatter based on configuration string parameter
            formatter = logging.Formatter(log_format)
            for handler in logger.handlers:
                handler.setFormatter(formatter)
        return logger

    # Format config
    # Fallback to default output pattern if format is empty
    fmt_str = log_format or '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    # Instantiate default message layout format compilation helper
    formatter = logging.Formatter(fmt_str)

    # Console output handler (redirecting errors/warnings to stderr)
    import sys
    # Direct log messages target to standard system error stream handler
    console_handler = logging.StreamHandler(sys.stderr)  # Construct stream redirect target to sys.stderr output
    console_handler.setFormatter(formatter)  # Setup format output layout details on console handler
    logger.addHandler(console_handler)

    # Rotating file handler
    try:
        file_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=3, encoding=encoding)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)  # Register file logger handler helper module to application loggers
    except (OSError, PermissionError) as e:
        logger.warning(f"Could not initialize file logging handler: {e}. Logging only to standard console output.")  # Log initialization failure alert

    return logger

def get_log_filepath(logger: logging.Logger) -> Optional[str]:  # Retrieve filename attribute mapping from rotating logger instances
    """Utility to retrieve path of file handler log file."""
    for handler in logger.handlers:
        if isinstance(handler, RotatingFileHandler):
            return handler.baseFilename
    return None
