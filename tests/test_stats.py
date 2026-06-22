import unittest
import os
import csv
from stats import get_posture_stats

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
