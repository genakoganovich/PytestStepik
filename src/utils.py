# src/utils.py
import random

def is_even(number):
    """Возвращает True, если число четное, иначе False."""
    return number % 2 == 0

def get_random_number():
    return random.randint(1, 100)