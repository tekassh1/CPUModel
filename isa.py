from enum import Enum


class LispFunctions(str, Enum):
    LET = "let"
    PROGN = "progn"
    OR = "or"
    AND = "and"
    INCF = "incf"
    SETQ = "setq"
    INPUT = "input"
    READ = "read"
    PRINT = "print"
    LOOP = "loop"
    IF = "if"
    RETURN = "return"
    MOD = "mod"
    ZEROP = "zerop"
    PLUS = "+"
    MINUS = "-"
    MUL = "*"
    DIV = "/"
    GR = ">"
    LE = "<"
    EQ = "="
    LOE = "<="
    GOE = ">="
    FORMAT = "format"
    TERPRI = "terpri"


class Opcode(str, Enum):
    LOAD = 'load'
    STORE = 'store'
    ADD = 'add'
    SUB = 'sub'
    MUL = 'mul'
    READ = 'read'
    PRINT = 'print'
    JMP = 'jmp'
    HLT = 'halt'


class SExpression:
    def __init__(self, function, args):
        if args is None:
            self.args = []

        self.function = function
        self.args = args

    def __str__(self):
        return f"{{Opcode: {self.function}, args: {self.args}}}"

    def __repr__(self):
        return self.__str__()

# {Opcode: let, args: [{Opcode: , args: [{Opcode: , args: [{Opcode: , args: [{Opcode: , args: [{Opcode: , args: ['curr', '0']}]}]}]}, {Opcode: , args: [{Opcode: , args: [{Opcode: , args: [{Opcode: , args: ['sum', '0']}]}]}]}]}, {Opcode: progn, args: [{Opcode: loop, args: [{Opcode: if, args: [{Opcode: >, args: ['curr', '1000']}, {Opcode: return, args: None}, {Opcode: if, args: [{Opcode: or, args: [{Opcode: zerop, args: [{Opcode: mod, args: ['curr', '3']}]}, {Opcode: zerop, args: [{Opcode: mod, args: ['curr', '5']}]}]}, {Opcode: incf, args: ['sum', 'curr']}]}]}, {Opcode: incf, args: ['curr']}]}, {Opcode: print, args: ['sum']}]}]}
