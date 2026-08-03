import logging  # Import standard logging module capabilities
from logging.handlers import RotatingFileHandler  # Import standard rotating file log utility class
from typing import Optional  # Import Optional type annotation from typing module


def setup_logger(log_file: str = "posture_guard.log", level: int = logging.INFO, log_format: Optional[str] = None, encoding: str = "utf-8") -> logging.Logger:  # Setup centralized logger instance with default parameters initialization setup method
    """
    Configures and returns a logger that prints to the console and writes to a rotating log file.

    :param log_file: File name/path where log messages should be written.
    :param level: The threshold logging level.
    :return: Configured logging.Logger instance.
    """
    # Retrieve or register centralized application logger instance helper
    logger = logging.getLogger("PostureGuard")  # Retrieve application level logger instance identifier tag
    # Set minimum severity event logging threshold filter level
    logger.setLevel(level)  # Set minimum log filtering level bounds thresholds filter check rule

    # Avoid adding duplicate handlers if the logger has already been setup
    # Check if any logging handlers have already been configured
    if logger.handlers:  # Guard block validating handler existence check
        # Verify if an explicit format string is provided
        if log_format:  # Verify user provided explicit formatter settings parameter
            # Compile new formatter based on configuration string parameter
            formatter = logging.Formatter(log_format)  # Build format map pattern compiled helper instance
            for handler in logger.handlers:  # Iterate over active logger handlers  # Reconfigure format bounds templates on active logging handlers loop
                handler.setFormatter(formatter)
        return logger  # Return fully initialized logger module reference object

    # Format config settings layout
    # Fallback to default output pattern if format is empty
    fmt_str = log_format or '%(asctime)s [%(levelname)s] %(name)s: %(message)s'  # Fallback to standard logging pattern template pattern
    # Instantiate default message layout format compilation helper
    formatter = logging.Formatter(fmt_str)  # Construct core system formatter compiler instance

    # Console output handler (redirecting errors/warnings to stderr stream)
    import sys  # Import sys module dynamically inside logger configuration setups module import
    # Direct log messages target to standard system error stream handler object
    console_handler = logging.StreamHandler(sys.stderr)  # Construct stream redirect target to sys.stderr output handler
    console_handler.setFormatter(formatter)  # Setup format output layout details on console handler instance format helper
    logger.addHandler(console_handler)  # Add console handler stream

    # Rotating file handler parameter configuration setup try
    try:
        file_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=3, encoding=encoding)  # Construct rotating file logs backup storage writer helper
        file_handler.setFormatter(formatter)  # Bind layout format parser properties onto file writer instance
        logger.addHandler(file_handler)  # Register file logger handler helper module to application loggers stream registry
    except (OSError, PermissionError) as e:
        logger.warning(f"Could not initialize file logging handler: {e}. Logging only to standard console output.")  # Log initialization failure alert warnings message

    return logger

def get_log_filepath(logger: logging.Logger) -> Optional[str]:  # Retrieve filename attribute mapping from rotating logger instances helper
    """Utility to retrieve path of file handler log file."""
    for handler in logger.handlers:
        if isinstance(handler, RotatingFileHandler):  # Filter log handler checks by RotatingFileHandler type subclasses
            return handler.baseFilename  # Extract file path location metadata parameters
    return None  # Return None if RotatingFileHandler is not configured fallback
