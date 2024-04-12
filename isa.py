from enum import Enum

functions = ["let", "progn", 'or', 'and', 'incf', 'setq', 'input', 'read', 'print', 'loop', 'if', 'return', 'mod', 'zerop',
             '+', '-', '*', '/', '>', '<', '=', '<=', '>=', 'format', 'terpri', 'end-of-file', 'handler-case']

# class Opcode(Enum):
#     LET = "let"
#     PROGN = "progn"
#     LOOP = "loop"
#     IF = "if"
#     OR = "or"
#     AND = "and"
#     INCF = "incf"
#     PRINT = "print"
#     PLUS = "+"
#     MINUS = "-"
#     MUL = "*"
#     DIV = "/"
#     EQ = "="
#     LS = "<"
#     MR = ">"
#     LEQ = "<="
#     MEQ = ">="

class Opcode(str, Enum):
    """Opcode для ISA."""
    LOAD = 'load'
    LOAD_CONST = 'loadc'
    LOAD_INDIRECT = 'load_indir'
    STORE = 'store'
    STORE_INDIRECT = 'store_indir'
    ADD = 'add'
    ADD_CONST = 'addc'
    SUB = 'sub'
    PRINT = 'print'
    PRINT_INT = 'print_int'
    READ = 'read'
    JMP = 'jmp'
    JE = 'je'
    JNE = 'jne'
    JG = 'jg'
    JL = 'jl'
    HLT = 'halt'

class Instruction:
    def __init__(self, opcode, args):
        if args is None:
            self.args = []

        self.opcode = opcode
        self.args = args

    def __str__(self):
        return f"{{Opcode: {self.opcode}, args: {self.args}}}"

    def __repr__(self):
        return self.__str__()
        # # args_str = ', '.join(map(str, self.args))
        # return f"{{Opcode: {self.opcode}, args: [{args_str}]}}"