

import contextlib
import io
import logging
import os
import tempfile

import pytest

import machine
import translator


@pytest.mark.golden_test("golden/*.yml")
def test_whole_by_golden(golden, caplog):
    # Установим уровень отладочного вывода на DEBUG
    caplog.set_level(logging.DEBUG)

    # Создаём временную папку для тестирования приложения.
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        # Готовим имена файлов для входных и выходных данных.
        source = os.path.join(tmp_dir_name, "source.asm")
        input_stream = os.path.join(tmp_dir_name, "input.txt")
        target = os.path.join(tmp_dir_name, "target.out")

        # Записываем входные данные в файлы. Данные берутся из теста.
        with open(source, "w", encoding="utf-8") as file:
            file.write(golden["source"])
        with open(input_stream, "w", encoding="utf-8") as file:
            file.write(golden["input"])

        # Запускаем транслятор и собираем весь стандартный вывод в переменную
        # stdout
        with contextlib.redirect_stdout(io.StringIO()) as stdout:
            translator.main([source, target])
            print("============================================================")
            machine.main([target, input_stream])

        # Выходные данные также считываем в переменные.
        with open(target, encoding="utf-8") as file:
            code = file.read()

        # Проверяем что ожидания соответствуют реальности.
        assert code == golden.out["code"]
        assert stdout.getvalue() == golden.out["output"]
        assert caplog.text == golden.out["log"]
