# Public starter example

The `afrisol_open_source.localization` module demonstrates basic language-tag normalization and fallback selection for applications serving multilingual audiences. It is **not** a full localization engine, translation service, or a production security boundary.

```python
from afrisol_open_source import supported_language

print(supported_language('sw-KE'))  # sw
print(supported_language('de-DE'))  # en (fallback)
```

Install locally with `python -m pip install -e .` and run tests with `python -m unittest discover -s tests -v`.
