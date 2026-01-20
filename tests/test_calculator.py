# tests/test_calculator.py
import pytest, sys

# 1. Импортируем нашу функцию из папки src
from src.calculator import add, divide

# 2. Пишем тестовую функцию, соблюдая правило именования
@pytest.mark.smoke
def test_add():
    # 3. Используем assert для проверки
    assert add(2, 3) == 5

@pytest.mark.regression
def test_divide():
    assert divide(10, 2) == 5

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

def test_add_raises_type_error_on_string_input():
    with pytest.raises(TypeError):
        add(5, "hello")


@pytest.mark.regression
def test_divide_by_zero_raises_value_error_with_message():
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)

    # Проверяем, что текст ошибки содержит нужную фразу
    assert "Нельзя делить на ноль" in str(excinfo.value)


@pytest.mark.slow
def test_very_slow_calculation():
    """Гипотетический тест, который работает очень долго."""
    # для примера просто сделаем его успешным
    assert True


@pytest.mark.smoke
@pytest.mark.regression
def test_critical_function():
    # Этот тест является и дымовым, и регрессионным
    assert True


@pytest.mark.skip(reason="Эта функциональность будет реализована в версии 2.0")
def test_subtraction():
    """Тест для будущей функции вычитания."""
    # assert subtract(10, 5) == 5
    pass


@pytest.mark.skipif(sys.version_info < (3, 15), reason="Требуется Python 3.15 или выше")
def test_new_python_feature():
    """Тест, использующий синтаксис, доступный только в новых версиях Python."""
    # Пример использования match-case, который появился в 3.10
    result = 0
    match 1:
        case 1:
            result = 1
    assert result == 1


@pytest.mark.xfail(reason="Известный баг с точностью float, будет исправлен в #TICKET-123")
def test_add_floats_bug():
    # Этот тест будет падать из-за особенностей представления float в Python
    assert add(0.1, 0.2) == 0.3