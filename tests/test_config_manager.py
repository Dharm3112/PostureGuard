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

    def test_log_rotation_validation(self) -> None:
        """Verifies validation catches invalid logging configuration values."""
        manager = ConfigManager()
        manager.set("log_max_bytes", 500)  # Min is 1024
        self.assertFalse(manager.validate_config())
        
        manager.set("log_max_bytes", 2048)
        manager.set("log_backup_count", 50)  # Max is 20
        self.assertFalse(manager.validate_config())

    def test_dict_initialization_overload(self) -> None:
        """Checks constructor logic when initial config dictionary is provided."""
        custom_config = {"camera_index": 7, "slouch_threshold_px": 80}
        manager = ConfigManager(initial_config=custom_config)
        self.assertEqual(manager.get("camera_index"), 7)
        self.assertEqual(manager.get("slouch_threshold_px"), 80)

    def test_validate_config_bounds(self) -> None:
        """Verifies config validation logic accepts standard settings and rejects bad settings."""
        manager = ConfigManager()
        self.assertTrue(manager.validate_config())
        
        # Test invalid threshold
        manager.set(ConfigManager.SLOUCH_THRESHOLD, 1)
        self.assertFalse(manager.validate_config())
        manager.set(ConfigManager.SLOUCH_THRESHOLD, 40)
        
        # Test invalid width
        manager.set(ConfigManager.CAMERA_WIDTH, 99999)
        self.assertFalse(manager.validate_config())

    def test_corrupted_config_fallback(self) -> None:
        """Checks ConfigManager falls back to defaults if config.json is corrupted."""
        # Write corrupted config.json
        with open("config.json", "w") as f:
            f.write("{invalid_json:")
        manager = ConfigManager()
        # Verify fallback loaded mock defaults (camera_index = 99)
        self.assertEqual(manager.get("camera_index"), 99)

    def test_reset_to_defaults(self) -> None:
        """Verifies config resetting capability."""
        manager = ConfigManager()
        manager.set("camera_index", 5)
        self.assertEqual(manager.get("camera_index"), 5)
        status = manager.reset_to_defaults()
        self.assertTrue(status)
        self.assertEqual(manager.get("camera_index"), 99)

    def test_get_config_filepath(self) -> None:
        """Verifies get_config_filepath returns the correct absolute path."""
        manager = ConfigManager()
        path = manager.get_config_filepath()
        self.assertTrue(os.path.isabs(path))
        self.assertTrue(path.endswith("config.json"))

    def test_invalid_frame_delay(self) -> None:
        """Verifies validation catches invalid frame delay settings."""
        manager = ConfigManager()
        manager.set(ConfigManager.FRAME_DELAY, 0)
        self.assertFalse(manager.validate_config())

    def test_invalid_alert_frames(self) -> None:
        """Verifies validation catches invalid time to alert frames settings."""
        manager = ConfigManager()
        manager.set(ConfigManager.TIME_TO_ALERT, 4)
        self.assertFalse(manager.validate_config())

if __name__ == "__main__":
    unittest.main()
