import csv  # Import standard csv parsing capabilities library package module engine
import os  # Import standard OS utility module helper package module engine
from typing import Dict, Any, Optional  # Import complex type hints for stats mapping hints types
BaseDirectory = os.path.dirname(os.path.abspath(__file__))  # Retrieve canonical parent root path directory settings checks path directory


def get_posture_stats(filepath: str = "posture_history.csv", start_date: Optional[str] = None, end_date: Optional[str] = None) -> Dict[str, Any]:  # Calculate aggregate posture statistics function
    """
    Parses the posture history CSV file and returns aggregate statistics.

    :param filepath: File path to the posture history CSV file.
    :return: Dictionary containing calculated posture statistics.
    """
    from logger_config import setup_logger
    logger = setup_logger()  # Setup logger instance for statistics parsing
    logger.debug(f"Calculating posture stats for file: {filepath}")  # Debug log file path target
    # Initializing default return values data structure mapping container keys
    stats = {  # Initialize posture statistics tracking dict
        "total_records": 0,  # Initialize total records count tracker record count
        "good_count": 0,  # Initialize good count tracker count
        "slouch_count": 0,  # Initialize slouch count tracker count
        "good_percent": 0.0,  # Initialize good posture percentage ratio metric
        "slouch_percent": 0.0,  # Initialize slouch posture percentage ratio metric
        "avg_deviation": 0.0
    }

    # Guard statement checking file existence bounds target path config
    if not os.path.exists(filepath):  # Guard clause against missing stats log file path targets check item
        return stats  # Return empty stats on error  # Return computed statistics dictionary

    total_deviation = 0  # Cumulative tracking for head tracking deviation pixels total tracker count variable
    try:  # Try block handling potential OSError during stats file parsing
        with open(filepath, "r", newline="", encoding="utf-8") as f:  # Open history logs csv stream in text reading mode
            # Parse target stream via csv dictionary mapping rows handler
            reader = csv.DictReader(f)  # Parse target stream via csv dictionary mapping rows handler engine class item
            for row in reader:  # Iterate over history rows
                # Validate row contents integrity checks header
                if not row or not row.get("timestamp"):  # Validate non-empty row timestamp check
                    continue
                ts = row.get("timestamp")  # Extract date string for time boundaries verification checks value string item
                # Apply chronological limits on start date
                if start_date and ts < start_date:  # Filter out timestamps before start date boundary check item
                    continue
                # Apply end dates boundary check thresholds limit
                if end_date and ts > end_date:  # Filter out timestamps after end date boundary check item limit
                    continue
                stats["total_records"] += 1  # Increment record count tracker value
                # Attempt integer numeric conversion checks safely
                try:
                    dev = int(row.get("deviation_px", 0))  # Convert deviation to integer value item
                    total_deviation += dev  # Accumulate deviation pixel offset count item
                except (ValueError, TypeError):  # Silence deviation conversion errors
                    pass

                state = row.get("state", "Good")  # Retrieve posture state label coordinate classification values label string
                if state == "Good":  # Verify if logged state is good posture count check
                    stats["good_count"] += 1  # Increment good posture count tracker value
                else:
                    stats["slouch_count"] += 1  # Increment slouch posture count tracker value
    except OSError as e:  # Catch file read errors
        from logger_config import setup_logger
        setup_logger().error(f"Failed to read posture history file: {e}")  # Log error on failure
        return stats

    total = stats["total_records"]  # Cache total records logged count value parameter item count
    if total > 0:  # Compute percentage metrics if records exist
        stats["good_percent"] = round((stats["good_count"] / total) * 100.0, 2)  # Compute good posture percentage value metric
        stats["slouch_percent"] = round((stats["slouch_count"] / total) * 100.0, 2)  # Compute slouch posture percentage value metric
        stats["avg_deviation"] = round(total_deviation / total, 2)  # Compute average deviation in pixels metric value

    return stats

def reset_statistics_file(filepath: str = "posture_history.csv") -> bool:  # Re-initialize history CSV log file with column headers function
    """Re-creates the history log file with header columns."""
    try:
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)  # Instantiate CSV writer for header initialization
            writer.writerow(["timestamp", "deviation_px", "state"])
        return True  # Return boolean validation flags indicating success status code value
    except OSError:
        return False
