import pytest
import requests
from src.api import get_data

def test_get_data(mocker):
    # Настраиваем мок так, чтобы он вызывал ошибку,
    # как это делает реальный `requests`.
    mocker.patch(
        "src.api.requests.get",
        side_effect=requests.exceptions.ConnectionError("API is down")
    )

    # Проверяем, что наша функция корректно "пробрасывает"
    # эту ошибку наверх.
    with pytest.raises(requests.exceptions.ConnectionError):
        get_data()