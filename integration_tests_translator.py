import unittest

import isa
import translator


def start(input_file, output_file, correct_file):
    translator.main([input_file, output_file])
    result = isa.read_code(output_file)
    correct_code = isa.read_code(correct_file)
    assert result == correct_code


class TestTranslator(unittest.TestCase):
    def test_prob1(self):
        start(
            "examples/prob1.asm",
            "examples/prob1_code.out",
            "examples/test_prob1_code.out",
        )

    def test_cat(self):
        start("examples/cat.asm", "examples/cat_code.out", "examples/test_cat_code.out")

    def test_hello_user(self):
        start(
            "examples/hello_user.asm",
            "examples/hello_user_code.out",
            "examples/test_hello_user_code.out",
        )

    def test_hello_world(self):
        start(
            "examples/hello.asm",
            "examples/hello_code.out",
            "examples/test_hello_code.out",
        )
