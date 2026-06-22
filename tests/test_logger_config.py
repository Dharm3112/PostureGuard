import unittest
import os
import logging
from logger_config import setup_logger

class TestLoggerConfig(unittest.TestCase):
    def test_logger_setup(self) -> None:
        test_log = "test_setup.log"
        if os.path.exists(test_log):
            os.remove(test_log)
        logger = setup_logger(test_log, logging.DEBUG)
        self.assertEqual(logger.name, "PostureGuard")
        
        # Shutdown file handler so we can delete the file safely
        for handler in logger.handlers[:]:
            if isinstance(handler, logging.FileHandler):
                handler.close()
                logger.removeHandler(handler)
        if os.path.exists(test_log):
            os.remove(test_log)

if __name__ == "__main__":
    unittest.main()
