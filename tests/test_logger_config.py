import unittest
import os
import logging
from logger_config import setup_logger

class TestLoggerConfig(unittest.TestCase):
    def setUp(self) -> None:
        logger = logging.getLogger("PostureGuard")
        for handler in logger.handlers[:]:
            handler.close()
            logger.removeHandler(handler)

    def test_custom_formatter(self) -> None:
        """Tests custom logging format creation."""
        test_log = "test_formatter.log"
        logger = setup_logger(test_log, logging.DEBUG, log_format="%(message)s")
        for handler in logger.handlers:
            if isinstance(handler, logging.FileHandler):
                self.assertEqual(handler.formatter._fmt, "%(message)s")
                handler.close()
                logger.removeHandler(handler)
        # Cleanup after formatting test runs
        if os.path.exists(test_log):
            os.remove(test_log)

    # Test double setup safety bounds checks
    def test_logger_encoding(self) -> None:
        """Tests logger file encoding config settings."""
        test_log = "test_encoding.log"
        logger = setup_logger(test_log, logging.DEBUG, encoding="ascii")
        for handler in logger.handlers:
            if isinstance(handler, logging.FileHandler):
                self.assertEqual(handler.encoding, "ascii")
                handler.close()
                logger.removeHandler(handler)
        if os.path.exists(test_log):
            os.remove(test_log)

    def test_logger_setup(self) -> None:
        test_log = "test_setup.log"
        if os.path.exists(test_log):
            os.remove(test_log)
        logger = setup_logger(test_log, logging.DEBUG)
        self.assertEqual(logger.name, "PostureGuard")
        
        # Shut down specific logging handlers safely to close open file locks
        for handler in logger.handlers[:]:
            if isinstance(handler, logging.FileHandler):
                handler.close()
                logger.removeHandler(handler)
        if os.path.exists(test_log):
            os.remove(test_log)

if __name__ == "__main__":
    unittest.main()
