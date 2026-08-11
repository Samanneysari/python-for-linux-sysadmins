from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from sysadmintools.inventory import filesystem_record, parse_os_release


class InventoryTests(TestCase):
    def test_parse_os_release(self) -> None:
        with TemporaryDirectory() as directory:
            path = Path(directory) / "os-release"
            path.write_text(
                'ID=rocky\nVERSION_ID="9.6"\nPRETTY_NAME="Rocky Linux 9.6"\n',
                encoding="utf-8",
            )
            result = parse_os_release(path)
        self.assertEqual(result["ID"], "rocky")
        self.assertEqual(result["VERSION_ID"], "9.6")
        self.assertEqual(result["PRETTY_NAME"], "Rocky Linux 9.6")

    def test_filesystem_record_has_valid_percent(self) -> None:
        with TemporaryDirectory() as directory:
            result = filesystem_record(Path(directory))
        self.assertGreater(result["total_bytes"], 0)
        self.assertGreaterEqual(result["used_percent"], 0)
        self.assertLessEqual(result["used_percent"], 100)
