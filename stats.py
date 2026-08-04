import csv  # Import standard csv parsing capabilities library package
import os  # Import standard OS utility module helper
from typing import Dict, Any, Optional  # Import complex type hints for stats mapping
BaseDirectory = os.path.dirname(os.path.abspath(__file__))  # Retrieve canonical parent root path directory settings checks


def get_posture_stats(filepath: str = "posture_history.csv", start_date: Optional[str] = None, end_date: Optional[str] = None) -> Dict[str, Any]:
    """
    Parses the posture history CSV file and returns aggregate statistics.

    :param filepath: File path to the posture history CSV file.
    :return: Dictionary containing calculated posture statistics.
    """
    from logger_config import setup_logger
    logger = setup_logger()
    logger.debug(f"Calculating posture stats for file: {filepath}")  # Debug log file path
    # Initializing default return values data structure mapping container keys
    stats = {  # Initialize posture statistics tracking dict
        "total_records": 0,
        "good_count": 0,
        "slouch_count": 0,
        "good_percent": 0.0,
        "slouch_percent": 0.0,
        "avg_deviation": 0.0
    }

    # Guard statement checking file existence bounds target path config
    if not os.path.exists(filepath):  # Guard clause against missing stats log file path targets check
        return stats  # Return empty stats on error  # Return computed statistics dictionary

    total_deviation = 0  # Cumulative tracking for head tracking deviation pixels total tracker
    try:  # Try block handling potential OSError during stats file parsing
        with open(filepath, "r", newline="", encoding="utf-8") as f:  # Open history logs csv stream in text reading mode
            # Parse target stream via csv dictionary mapping rows handler
            reader = csv.DictReader(f)  # Parse target stream via csv dictionary mapping rows handler engine class
            for row in reader:  # Iterate over history rows
                # Validate row contents integrity checks header
                if not row or not row.get("timestamp"):  # Validate non-empty row timestamp
                    continue
                ts = row.get("timestamp")  # Extract date string for time boundaries verification checks value
                # Apply chronological limits on start date
                if start_date and ts < start_date:  # Filter out timestamps before start date boundary
                    continue
                # Apply end dates boundary check thresholds limit
                if end_date and ts > end_date:  # Filter out timestamps after end date boundary check
                    continue
                stats["total_records"] += 1  # Increment record count
                # Attempt integer numeric conversion checks safely
                try:
                    dev = int(row.get("deviation_px", 0))  # Convert deviation to integer
                    total_deviation += dev  # Accumulate deviation pixel offset
                except (ValueError, TypeError):  # Silence deviation conversion errors
                    pass

                state = row.get("state", "Good")  # Retrieve posture state label coordinate classification values label
                if state == "Good":  # Verify if logged state is good posture count check
                    stats["good_count"] += 1  # Increment good posture count
                else:
                    stats["slouch_count"] += 1  # Increment slouch posture count
    except OSError as e:  # Catch file read errors
        from logger_config import setup_logger
        setup_logger().error(f"Failed to read posture history file: {e}")  # Log error on failure
        return stats

    total = stats["total_records"]  # Cache total records logged count value parameter item
    if total > 0:  # Compute percentage metrics if records exist
        stats["good_percent"] = round((stats["good_count"] / total) * 100.0, 2)  # Compute good posture percentage value
        stats["slouch_percent"] = round((stats["slouch_count"] / total) * 100.0, 2)  # Compute slouch posture percentage value
        stats["avg_deviation"] = round(total_deviation / total, 2)

    return stats

def reset_statistics_file(filepath: str = "posture_history.csv") -> bool:  # Reconstruct clean CSV files containing only headers schema layout
    """Re-creates the history log file with header columns."""
    try:
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "deviation_px", "state"])
        return True  # Return boolean validation flags indicating success status code
    except OSError:
        return False
