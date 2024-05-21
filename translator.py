import sys
from isa import Opcode, write_code

command2opcode = {
    'in': Opcode.IN,
    'out': Opcode.OUT,
    'out#': Opcode.OUT_REL,
    'out_char': Opcode.OUT_CHAR,
    'jmp': Opcode.JMP,
    'hlt': Opcode.HLT,
    'mov': Opcode.MOV,
    'cmp': Opcode.CMP,
    'cmp*': Opcode.CMP_REL_INC,
    'je': Opcode.JE,
    'rdiv': Opcode.RDIV,
    'add': Opcode.ADD,
    'sub': Opcode.SUB,
    'mul': Opcode.MUL,
    'div': Opcode.DIV,
    'save': Opcode.SAVE
}
def translate(text):
    code = []
    labels = {}
    variables = {}
    data_in_progress = False
    section_text_in_progress = False
    text_presented = False
    addr_counter = -1
    data = []

    for line in text.split("\n"):
        line = line.strip()
        if line == '' or line.startswith(';'):
            continue

        # Reset the address counter once the .text section is reached
        if line.strip() == ".text:":
            addr_counter = -1
            text_presented = True

        if line.startswith('.'):
            continue

        addr_counter += 1

        line_words = line.split()
        for word in line_words:
            word = word.strip()

            if word[0] != '.' and word[-1] == ':':
                assert word[:-1] not in labels, "Label " + word[:-1] + " is already presented!"
                labels[word[:-1]] = addr_counter

    assert text_presented, "Section .text is not presented!"

    addr_counter = -1

    for line in text.split("\n"):
        line = line.strip()
        if line == "" or line.startswith(';'):
            continue

        if line == ".data:":
            data_in_progress = True
            section_text_in_progress = False
            addr_counter = -1
            continue

        if line == ".text:":
            data_in_progress = False
            section_text_in_progress = True
            addr_counter = -1
            continue

        if data_in_progress:
            # section data translation
            line = line.replace(":", "")
            variable = line.split(maxsplit=2)
            if len(variable) < 2:
                continue
            assert variable[1] not in variables, "variable is already assigned!"

            if variable[0] == "str":
                if len(variable) == 3:
                    variable[2] = variable[2][1:-1]
                    strlen = -1
                    for char in variable[2].split(', '):
                        if char:
                        # char = char.replace("'", "")  # Remove single quotes from the character
                            strlen += 1
                            addr_counter += 1
                            if strlen == 0:
                                variables[variable[1]] = addr_counter
                            data.append(ord(char.strip("'")))  # Append ASCII value of the character to data
                    addr_counter += 1
                    data.append(ord('\u0000'))
            else:
                addr_counter += 1
                variables[variable[1]] = addr_counter
                if len(variable) == 3:
                    data.append(int(variable[2]))


        elif section_text_in_progress:
            args = []
            command = line.split()
            command_start_index = 0
            addr_counter += 1
            if command[0][-1] == ":":
                command_start_index = 1

            for i in range(command_start_index + 1, len(command)):
                if command[i][0] == '[' and command[i][-1] == ']':
                    if command[i][1:-1] in variables:
                        data.append(variables[command[i][1:-1]])
                        args.append(len(data) - 1)
                else:
                    if command[i] in variables:
                        args.append(variables[command[i]])
                    elif command[i] in labels:
                        args.append(labels[command[i]])
                    else:
                        try:
                            int(command[i])
                            data.append(command[i])
                            args.append(len(data) - 1)
                        except ValueError:
                            pass

            code.append({"opcode": command2opcode[command[command_start_index]],
                         "addr": addr_counter,
                         "args": args})

    return code, data


def main(args):
    assert len(args) == 2, \
        "Wrong arguments: translator.py <input_file> <target_file>"
    source, target = args

    with open(source, "rt", encoding="utf-8") as f:
        source = f.read()

    code, data = translate(source)
    print("source LoC:", len(source.split()), "code instr:", len(code))
    write_code(target, code, data)

if __name__ == '__main__':
    main(sys.argv[1:])
