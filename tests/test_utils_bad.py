# tests/test_utils_bad.py (Пример плохого, повторяющегося кода)

from src.utils import is_even

def test_is_even_positive_even():
    assert is_even(2) is True

def test_is_even_positive_odd():
    assert is_even(3) is False

def test_is_even_zero():
    assert is_even(0) is True

def test_is_even_negative_even():
    assert is_even(-4) is True

def test_is_even_negative_odd():
    assert is_even(-5) is False

# ... и так далее для чисел 6, 7, 8, -10, -11...