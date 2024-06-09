from enum import Enum


class AsmFunctions(str, Enum):
    MOV = 'mov'
    LD = 'ld'
    ST = 'st'
    INC = 'inc'
    DEC = 'dec'
    NEG = 'neg'
    ADD = 'add'
    DIV = 'div'
    MOD = 'mod'
    CMP = 'cmp'
    JMP = 'jmp'
    JG = 'jg'
    JE = 'je'
    JL = 'jl'

    def __str__(self):
        return self.name

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
