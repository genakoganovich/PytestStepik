import sys
import types
import pytest

def test_log_message_stab(monkeypatch, mocker):
    # 1️⃣ создаём фейковый модуль external_logger
    fake_external_logger = types.ModuleType("external_logger")

    # 2️⃣ добавляем mock для метода send
    fake_external_logger.send = mocker.Mock()

    # 3️⃣ подсовываем его Python через monkeypatch
    monkeypatch.setitem(sys.modules, "external_logger", fake_external_logger)

    # 4️⃣ теперь безопасно импортировать log_message
    from src.logger import log_message

    # 5️⃣ вызываем функцию
    log_message("hello")

    # 6️⃣ проверяем вызов
    fake_external_logger.send.assert_called_once_with("hello")
