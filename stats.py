import csv
import os
from typing import Dict, Any


def get_posture_stats(filepath: str = "posture_history.csv") -> Dict[str, Any]:
    """
    Parses the posture history CSV file and returns aggregate statistics.

    :param filepath: File path to the posture history CSV file.
    :return: Dictionary containing calculated posture statistics.
    """
    stats = {
        "total_records": 0,
        "good_count": 0,
        "slouch_count": 0,
        "good_percent": 0.0,
        "slouch_percent": 0.0,
        "avg_deviation": 0.0
    }

    if not os.path.exists(filepath):
        return stats

    total_deviation = 0
    try:
        with open(filepath, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
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
    except OSError:
        return stats

    total = stats["total_records"]
    if total > 0:
        stats["good_percent"] = (stats["good_count"] / total) * 100.0
        stats["slouch_percent"] = (stats["slouch_count"] / total) * 100.0
        stats["avg_deviation"] = total_deviation / total

    return stats
