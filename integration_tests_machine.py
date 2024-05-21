
import unittest

import machine
import translator


def start(source_code, output_file, input_file):
    translator.main([source_code, output_file])
    if input_file == "":
        return machine.main([output_file])
    return machine.main([output_file, input_file])


class TestMachine(unittest.TestCase):

    def test_hello(self):
        output = start("examples/hello.asm", "examples/hello_code.out", "")
        assert output == "Hello world!"

    def test_cat(self):
        output = start("examples/cat.asm", "examples/cat_code.out", "examples/input.txt")
        assert output == "Good day!"

    def test_prob1(self):
        output = start("examples/prob1.asm", "examples/prob1_code.out", "")
        print(output)
        assert output == '233168'

