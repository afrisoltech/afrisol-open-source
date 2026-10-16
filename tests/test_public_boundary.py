import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('boundary', Path(__file__).parents[1] / 'scripts/public_boundary.py')
boundary = importlib.util.module_from_spec(spec)
spec.loader.exec_module(boundary)


class PublicBoundaryTests(unittest.TestCase):
    def test_rejects_private_paths(self):
        for name in ['.env', '.env.production', 'infra/terraform.tfstate', 'keys/server.pem', 'customer-data/export.csv']:
            with self.subTest(name=name), self.assertRaises(ValueError):
                boundary.validate_file(name, b'example')

    def test_rejects_secret_values(self):
        samples = [b'-----BEGIN ' + b'PRIVATE KEY-----', b'AKIA' + b'Z' * 16, b'ghp_' + b'z' * 36,
                   b'client_secret = ' + b'"' + b'x' * 20 + b'"']
        for value in samples:
            with self.assertRaises(ValueError):
                boundary.validate_file('example.txt', value)

    def test_allows_ordinary_public_code(self):
        boundary.validate_file('src/utility.py', b'def add(a, b): return a + b\n')

    def test_rejects_binary_and_large_files(self):
        for value in [b'a\x00b', b'x' * (1024 * 1024 + 1)]:
            with self.assertRaises(ValueError):
                boundary.validate_file('sample.txt', value)
