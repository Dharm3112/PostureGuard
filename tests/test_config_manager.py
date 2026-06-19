import unittest
import os
import shutil
import json
from config_manager import ConfigManager


class TestConfigManager(unittest.TestCase):
    """
    Unit tests for ConfigManager.
    """
    def setUp(self) -> None:
        # Backup existing config files if they exist to avoid corruption during testing
        self.backup_local = "config.json.bak"
        self.backup_default = "config.json.default.bak"
        
        if os.path.exists("config.json"):
            shutil.move("config.json", self.backup_local)
        if os.path.exists("config.json.default"):
            shutil.copy("config.json.default", self.backup_default)
            
        # Create a mock default config file
        self.mock_defaults = {
            "camera_index": 99,
            "slouch_threshold_px": 55,
            "time_to_alert_frames": 100,
            "frame_delay_ms": 30,
            "camera_width": 320,
            "camera_height": 240,
            "save_history": False,
            "saved_baseline_y": None
        }
        with open("config.json.default", "w") as f:
            json.dump(self.mock_defaults, f)

    def tearDown(self) -> None:
        # Clean up files created during test
        if os.path.exists("config.json"):
            os.remove("config.json")
        if os.path.exists("config.json.default"):
            os.remove("config.json.default")
            
        # Restore backups
        if os.path.exists(self.backup_local):
            shutil.move(self.backup_local, "config.json")
        if os.path.exists(self.backup_default):
            shutil.move(self.backup_default, "config.json.default")

    def test_ensure_config_exists_copies_default(self) -> None:
        """Verifies ConfigManager copies config.json.default if config.json doesn't exist."""
        manager = ConfigManager()
        self.assertTrue(os.path.exists("config.json"))
        self.assertEqual(manager.get("camera_index"), 99)
        self.assertEqual(manager.get("slouch_threshold_px"), 55)

    def test_get_and_set_values(self) -> None:
        """Verifies getter and setter functions modify config on disk."""
        manager = ConfigManager()
        manager.set("camera_index", 2)
        self.assertEqual(manager.get("camera_index"), 2)
        
        # Read from disk to check persistence
        with open("config.json", "r") as f:
            data = json.load(f)
        self.assertEqual(data["camera_index"], 2)

    def test_reset_to_defaults(self) -> None:
        """Verifies config resetting capability."""
        manager = ConfigManager()
        manager.set("camera_index", 5)
        self.assertEqual(manager.get("camera_index"), 5)
        manager.reset_to_defaults()
        self.assertEqual(manager.get("camera_index"), 99)


if __name__ == "__main__":
    unittest.main()
