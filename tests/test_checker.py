# tests/test_checker.py
import pytest

from src.checker import check_sign

@pytest.mark.parametrize("n, expected", [
    pytest.param(10, "positive", id="positive_numbers"),
    pytest.param(-5, "zero or negative", id="zero or negative")
])
def test_check_sign_positive(n, expected):
    assert check_sign(n) == expected