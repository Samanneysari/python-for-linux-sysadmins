from unittest import TestCase

from sysadmintools.service_check import parse_properties, validate_unit


class ServiceCheckTests(TestCase):
    def test_parse_properties_preserves_equals_in_value(self) -> None:
        result = parse_properties("LoadState=loaded\nDescription=a=b\n")
        self.assertEqual(result["LoadState"], "loaded")
        self.assertEqual(result["Description"], "a=b")

    def test_valid_unit(self) -> None:
        self.assertEqual(validate_unit("sshd@demo.service"), "sshd@demo.service")

    def test_rejects_option_like_unit(self) -> None:
        with self.assertRaises(ValueError):
            validate_unit("--system")

    def test_rejects_whitespace(self) -> None:
        with self.assertRaises(ValueError):
            validate_unit("bad unit.service")
