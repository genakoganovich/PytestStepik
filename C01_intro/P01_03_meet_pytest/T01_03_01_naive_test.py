# naive_test.py
from EX01_03_01_calculator import add

# Проверка 1
result1 = add(2, 3)
if result1 == 5:
    print("Проверка 1: Успех")
else:
    print(f"Проверка 1: ПРОВАЛ! Ожидали 5, получили {result1}")

# Проверка 2
result2 = add(-1, 1)
if result2 == 0:
    print("Проверка 2: Успех")
else:
    print(f"Проверка 2: ПРОВАЛ! Ожидали 0, получили {result2}")

# ... и так далее для десятков других проверок