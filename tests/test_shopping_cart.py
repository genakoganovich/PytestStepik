# tests/test_shopping_cart.py
import pytest


# Вспомогательный класс для нашего примера
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def get_total_price(self):
        return sum(self.items.values())

# 1. Pytest находит эту функцию и "регистрирует" ее как фикстуру
#    с именем 'filled_cart'.
# 1. Создаем фикстуру
@pytest.fixture
def filled_cart():
    """Создает и возвращает корзину с двумя товарами."""
    # 2. Здесь находится наш код ПОДГОТОВКИ (Setup)
    cart = ShoppingCart()
    cart.add_item("apple", price=10)
    cart.add_item("banana", price=20)
    # 3. Возвращаем подготовленный объект
    return cart


# 4. Пишем тест, который ЗАПРАШИВАЕТ фикстуру
def test_add_item(filled_cart):
    # `filled_cart` здесь - это тот самый объект `cart`,
    # который вернула наша фикстура
    filled_cart.add_item("cherry", price=30)
    assert "cherry" in filled_cart.items


# 2. Pytest находит этот тест.
# 3. Он смотрит на его аргументы и видит 'filled_cart'.
# 4. Он говорит: "Ага, мне нужна фикстура с таким именем!"
def test_get_total_price(filled_cart):
    # Мы можем использовать ту же самую фикстуру в другом тесте!
    # 5. К моменту, когда эта строка начнет выполняться,
    #    Pytest уже выполнил фикстуру 'filled_cart'
    #    и передал ее результат в эту переменную.
    #    То есть, 'filled_cart' здесь - это уже готовый объект корзины.

    # Мы можем работать с ним как с обычным объектом
    assert filled_cart.get_total_price() == 30