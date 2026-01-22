# tests/conftest.py
import pytest
# Предположим, у нас есть такой модуль для работы с БД
import db_connector


@pytest.fixture(scope="session")
def db_connection():
    # --- SETUP ---
    # Этот код выполнится один раз в начале всего запуска
    print("\nУстановка соединения с БД...")
    connection = db_connector.connect("test_db_host")

    yield connection

    # --- TEARDOWN ---
    # Этот код выполнится один раз в самом конце всего запуска
    print("\nЗакрытие соединения с БД...")
    connection.close()


# Теперь любой тест в проекте может безопасно использовать эту фикстуру
def test_some_db_operation(db_connection):
    # ... использует `db_connection` ...
    assert True
