import unittest
import os
import csv
from stats import get_posture_stats, reset_statistics_file

class TestStats(unittest.TestCase):
    def setUp(self) -> None:
        self.filename = "test_history.csv"
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def tearDown(self) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_get_posture_stats_nonexistent(self) -> None:
        stats = get_posture_stats("nonexistent_file.csv")
        self.assertEqual(stats["total_records"], 0)

    def test_empty_file_stats(self) -> None:
        # Write only header
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "deviation_px", "state"])
        stats = get_posture_stats(self.filename)
        self.assertEqual(stats["total_records"], 0)
        self.assertEqual(stats["good_percent"], 0.0)

    def test_malformed_rows_stats(self) -> None:
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "deviation_px", "state"])
            writer.writerow(["", "", ""]) # Empty row
            writer.writerow(["2026-06-22 12:00:00", "invalid_dev", "Good"])
            writer.writerow(["2026-06-22 12:01:00", "50", "Slouching"])
            
        stats = get_posture_stats(self.filename)
        self.assertEqual(stats["total_records"], 2) # Empty row is skipped
        self.assertEqual(stats["good_count"], 1)
        self.assertEqual(stats["avg_deviation"], 25.0) # (0 + 50) / 2

    def test_date_range_filtering(self) -> None:
        """Tests stats filtering with dates bounds parameters."""
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "deviation_px", "state"])
            writer.writerow(["2026-06-22 12:00:00", "10", "Good"])
            writer.writerow(["2026-06-22 12:05:00", "20", "Good"])
            writer.writerow(["2026-06-22 12:10:00", "30", "Good"])
            
        stats = get_posture_stats(self.filename, start_date="2026-06-22 12:02:00", end_date="2026-06-22 12:08:00")
        self.assertEqual(stats["total_records"], 1)
        self.assertEqual(stats["avg_deviation"], 20.0)

    def test_reset_statistics_file_helper(self) -> None:
        """Verifies stats reset file creates clean header file."""
        status = reset_statistics_file(self.filename)
        self.assertTrue(status)
        stats = get_posture_stats(self.filename)
        self.assertEqual(stats["total_records"], 0)

    def test_get_posture_stats_valid(self) -> None:
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "deviation_px", "state"])
            writer.writerow(["2026-06-22 12:00:00", "10", "Good"])
            writer.writerow(["2026-06-22 12:01:00", "45", "Slouching"])
            
        stats = get_posture_stats(self.filename)
        self.assertEqual(stats["total_records"], 2)
        self.assertEqual(stats["good_count"], 1)
        self.assertEqual(stats["slouch_count"], 1)
        self.assertEqual(stats["good_percent"], 50.0)

if __name__ == "__main__":
    unittest.main()
