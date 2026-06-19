import os
import json
import shutil
from typing import Any, Dict


class ConfigManager:
    """
    Manages local application configuration JSON files.
    Copies default settings, reads config parameters, and handles runtime updates.
    """
    DEFAULT_CONFIG_FILE = "config.json.default"
    LOCAL_CONFIG_FILE = "config.json"

    def __init__(self) -> None:
        """
        Initializes the ConfigManager, ensuring that a local config.json exists.
        Loads the config into an in-memory dictionary.
        """
        self.config_data: Dict[str, Any] = {}
        self._ensure_config_exists()

    def _ensure_config_exists(self) -> None:
        """
        Helper method to copy config.json.default to config.json if the latter is missing.
        """
        if not os.path.exists(self.LOCAL_CONFIG_FILE):
            if os.path.exists(self.DEFAULT_CONFIG_FILE):
                shutil.copy(self.DEFAULT_CONFIG_FILE, self.LOCAL_CONFIG_FILE)
            else:
                # Fallback internal defaults if config.json.default is also missing
                self.config_data = {
                    "camera_index": 0,
                    "slouch_threshold_px": 40,
                    "time_to_alert_frames": 50,
                    "frame_delay_ms": 15,
                    "camera_width": 640,
                    "camera_height": 480,
                    "save_history": True,
                    "saved_baseline_y": None
                }
                self._save_to_file()
