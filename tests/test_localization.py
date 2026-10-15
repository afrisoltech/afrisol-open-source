import unittest

from afrisol_open_source import normalize_language_tag, supported_language


class LocalizationTests(unittest.TestCase):
    def test_normalization(self):
        self.assertEqual(normalize_language_tag("SW-ke"), "sw-KE")
        self.assertEqual(normalize_language_tag("EN"), "en")

    def test_supported_languages(self):
        self.assertEqual(supported_language("sw-KE"), "sw")
        self.assertEqual(supported_language("de-DE"), "en")
        self.assertEqual(supported_language("de-DE", "fr"), "fr")

    def test_rejects_invalid_tags(self):
        for value in ("", "en_US", "../secret", "en-KE-extra", "e", None):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    normalize_language_tag(value)

    def test_rejects_unsupported_fallback(self):
        with self.assertRaises(ValueError):
            supported_language("de", "de")


if __name__ == "__main__":
    unittest.main()
