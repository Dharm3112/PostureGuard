import csv
import os
from typing import Dict, Any, Optional
BaseDirectory = os.path.dirname(os.path.abspath(__file__))


def get_posture_stats(filepath: str = "posture_history.csv", start_date: Optional[str] = None, end_date: Optional[str] = None) -> Dict[str, Any]:
    """
    Parses the posture history CSV file and returns aggregate statistics.

    :param filepath: File path to the posture history CSV file.
    :return: Dictionary containing calculated posture statistics.
    """
    from logger_config import setup_logger
    logger = setup_logger()
    logger.debug(f"Calculating posture stats for file: {filepath}")
    # Initializing default return values data structure mapping container keys
    stats = {
        "total_records": 0,
        "good_count": 0,
        "slouch_count": 0,
        "good_percent": 0.0,
        "slouch_percent": 0.0,
        "avg_deviation": 0.0
    }

    # Guard statement checking file existence bounds target path config
    if not os.path.exists(filepath):
        return stats

    total_deviation = 0  # Cumulative tracking for head tracking deviation pixels
    try:
        with open(filepath, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row or not row.get("timestamp"):
                    continue
                ts = row.get("timestamp")
                if start_date and ts < start_date:
                    continue
                if end_date and ts > end_date:
                    continue
                stats["total_records"] += 1
                try:
                    dev = int(row.get("deviation_px", 0))
                    total_deviation += dev
                except (ValueError, TypeError):
                    pass

                state = row.get("state", "Good")
                if state == "Good":
                    stats["good_count"] += 1
                else:
                    stats["slouch_count"] += 1
    except OSError as e:
        from logger_config import setup_logger
        setup_logger().error(f"Failed to read posture history file: {e}")
        return stats

    total = stats["total_records"]
    if total > 0:
        stats["good_percent"] = round((stats["good_count"] / total) * 100.0, 2)
        stats["slouch_percent"] = round((stats["slouch_count"] / total) * 100.0, 2)
        stats["avg_deviation"] = round(total_deviation / total, 2)

    return stats

def reset_statistics_file(filepath: str = "posture_history.csv") -> bool:
    """Re-creates the history log file with header columns."""
    try:
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "deviation_px", "state"])
        return True
    except OSError:
        return False
