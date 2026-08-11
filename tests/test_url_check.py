from unittest import TestCase

from sysadmintools.url_check import validate_url


class URLValidationTests(TestCase):
    def test_accepts_allowlisted_https(self) -> None:
        url = "https://app.example.net/health"
        self.assertEqual(validate_url(url, {"app.example.net"}, False), url)

    def test_rejects_http_by_default(self) -> None:
        with self.assertRaises(ValueError):
            validate_url("http://app.example.net/", {"app.example.net"}, False)

    def test_rejects_credentials(self) -> None:
        with self.assertRaises(ValueError):
            validate_url("https://user:pass@app.example.net/", {"app.example.net"}, False)

    def test_rejects_non_allowlisted_host(self) -> None:
        with self.assertRaises(ValueError):
            validate_url("https://other.example.net/", {"app.example.net"}, False)
