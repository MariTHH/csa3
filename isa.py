"""Типы данных для представления и сериализации/десериализации машинного кода."""
import json
from enum import Enum


class Opcode(str, Enum):
    """Opcode для ISA."""

    HLT = "hlt"
    MOV = "mov"
    CMP = "cmp"
    CMP_REL_INC = "cmp_rel_inc"
    RDIV = "rdiv"
    ADD = "add"
    SUB = "sub"
    MUL = "mul"
    DIV = "div"
    INC = "inc"

    IN = "in"
    OUT = "out"
    OUT_CHAR = "out_char"
    OUT_REL = "out_rel"
    JMP = "jmp"
    JE = "je"
    SAVE = "save"


inst_to_mc = {
    "hlt": [17],
    "mov": [0, 3, 15],
    "cmp": [0, 6, 15],
    "cmp_rel_inc": [0, 2, 6, 12, 5, 15],
    "rdiv": [0, 7, 15],
    "add": [0, 8, 4, 15],
    "sub": [0, 9, 4, 15],
    "mul": [0, 10, 4, 15],
    "div": [0, 11, 4, 15],
    "in": [1, 15],
    "out": [0, 13, 15],
    "out_char": [0, 14, 15],
    "out_rel": [0, 2, 14, 15],
    "jmp": [16],
    "je": [18],
    "save": [4, 15],
}


def write_code(filename, code, data):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(code, indent=4))

    with open("data_section.txt", "w", encoding="utf-8") as file:
        file.write(json.dumps(data, indent=4))


def read_code(filename):
    with open(filename, encoding="utf-8") as file:
        code = json.loads(file.read())

    with open("data_section.txt", encoding="utf-8") as file:
        data_section = json.loads(file.read())

    return code, data_section
