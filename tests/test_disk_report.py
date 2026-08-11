from unittest import TestCase

from sysadmintools.disk_report import classify


class DiskReportTests(TestCase):
    def test_status_boundaries(self) -> None:
        self.assertEqual(classify(84.99, 85, 95), "ok")
        self.assertEqual(classify(85, 85, 95), "warning")
        self.assertEqual(classify(95, 85, 95), "critical")

    def test_rejects_bad_threshold_order(self) -> None:
        with self.assertRaises(ValueError):
            classify(50, 95, 85)

    def test_rejects_impossible_percent(self) -> None:
        with self.assertRaises(ValueError):
            classify(101, 85, 95)
