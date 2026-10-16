"""Fail closed on forbidden paths and common high-confidence secret patterns.

A review aid, not a claim that regexes can prove safe disclosure.
"""
from pathlib import Path
import re
import subprocess
import sys

DENIED = re.compile(r'(^|/)(?:\.env(?:\..*)?|terraform\.tfstate(?:\..*)?|[^/]*\.(?:pem|key|p12|pfx)|customer-data|supplier-credentials|private-export)(?:/|$)', re.I)
SECRETS = [
    re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    re.compile(rb'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b'),
    re.compile(rb'\bgh[pousr]_[A-Za-z0-9]{36,}\b'),
    re.compile(rb'\bgithub_pat_[A-Za-z0-9_]{40,}\b'),
    re.compile(rb'(?i)(?:password|client_secret|api_key|access_token)\s*[=:]\s*[\x22\x27][A-Za-z0-9/+_.-]{16,}[\x22\x27]'),
]

def validate_file(path, content):
    if DENIED.search(path):
        raise ValueError('Forbidden public path')
    if len(content) > 1024 * 1024:
        raise ValueError('Large file requires separate maintainer review')
    if b'\x00' in content:
        raise ValueError('Binary file requires separate maintainer review')
    if any(pattern.search(content) for pattern in SECRETS):
        raise ValueError('Potential secret; use private reporting')


def scan(root):
    paths = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().split('\0')
    errors = []
    for name in filter(None, paths):
        path = root / name
        try:
            if path.is_symlink():
                raise ValueError('Symlink requires separate maintainer review')
            validate_file(name, path.read_bytes())
        except (ValueError, OSError) as exc:
            errors.append(f'{name}: {exc}')
    if errors:
        raise ValueError('\n'.join(errors))


if __name__ == '__main__':
    try:
        scan(Path(__file__).resolve().parents[1])
    except ValueError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
    print('Public boundary checks passed; human licensing and disclosure review still required.')
