# tests/test_calculator.py

# 1. Импортируем нашу функцию из папки src
from src.calculator import add

# 2. Пишем тестовую функцию, соблюдая правило именования
def test_add():
    # 3. Используем assert для проверки
    assert add(2, 3) == 5

def test_example():
    pass

def test_addition():
    assert 5 + 5 == 10

def test_equality():
    assert 5 == 5

def test_inequality():
    assert 5 != 6

def test_greater_than():
    assert 10 > 5

def test_less_or_equal():
    assert 3 <= 3

def test_string_is_truthy():
    # Непустая строка - это True в логическом контексте
    assert "hello"

def test_list_is_truthy():
    # Непустой список - это True
    assert [1, 2, 3]

def test_empty_list_is_falsy():
    # Пустой список - это False в логическом контексте
    # not False -> True, поэтому assert проходит
    assert not []

def test_zero_is_falsy():
    assert not 0

def test_item_in_list():
    my_list = ["apple", "banana", "cherry"]
    assert "banana" in my_list

def test_substring_in_string():
    greeting = "Hello, world!"
    assert "world" in greeting

def test_complex_expression():
    x = 10
    assert x > 5 and x % 2 == 0

def test_add_with_wrong_expectation():
    """Этот тест специально написан так, чтобы провалиться."""
    # Вызываем функцию прямо внутри assert, чтобы увидеть детализацию ошибки
    assert add(2, 2) == 5