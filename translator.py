import re
import sys

from isa import LispFunctions, SExpression
from preprocessor import preprocess


def split_string_with_quotes(s):
    parts = re.findall(r'"[^"]*"|[^\s]+', s)
    return parts

def lisp_to_s_expr(source):
    source = source.strip()
    assert source[0] == '(' and source[-1] == ')', "Wrong brackets sequence"

    source = source[1: -1]
    if source == '':
        return SExpression(None, None)

    # Recursion endpoint - No brackets
    if not (('(' in source) or (')' in source)):
        terms = split_string_with_quotes(source)

        if len(terms) == 1:                                                                             # (val) case
            if terms[0] in LispFunctions:
                return SExpression(terms[0], None)
            else:
                return terms[0]
        elif len(terms) == 2:                                                                           # (var value) case
            if terms[0] in LispFunctions:
                return SExpression(terms[0], [terms[1]])
            return SExpression('', terms)

        assert (terms[0] in LispFunctions) or terms[0] == '',  f'Function {terms[0]} doesn\'t exist'    # (op arg1 arg2) case
        return SExpression(terms[0], terms[1: len(terms)])

    # Resolve args
    is_started = False

    start_idx = 0
    cntr = 0

    opcode = ""
    args = []

    for i in range(len(source)):
        if source[i] == '(':
            if not is_started:
                is_started = True
                start_idx = i
            cntr += 1
        elif source[i] == ')':
            cntr -= 1
            if cntr == 0:
                is_started = False
                if len(args) == 0:
                    opcode = source[0:start_idx].strip()
                    assert opcode in LispFunctions or opcode == '', f'Function {opcode} doesn\'t exist'

                args.append(lisp_to_s_expr(source[start_idx: i + 1]))

        assert cntr >= 0, "Wrong code format (missed brackets)"

    assert cntr == 0, "Wrong code format (extra brackets)"
    return SExpression(opcode, args)

def generate_machine_code(s_expression: SExpression):

    machine_instructions = []

    func = s_expression.function
    if func == '':
        if isinstance(s_expression.args, list):
            return s_expression.args
        elif isinstance(s_expression.args, SExpression):
            return generate_machine_code(s_expression.args)

    elif getattr(LispFunctions, "LET") == LispFunctions.LET:
        # define "let" func, call with given args to generate machine codes
        pass
    elif getattr(LispFunctions, "PROGN") == LispFunctions.PROGN:
        pass
    elif getattr(LispFunctions, "OR") == LispFunctions.OR:
        pass
    elif getattr(LispFunctions, "AND") == LispFunctions.AND:
        pass
    elif getattr(LispFunctions, "INCF") == LispFunctions.INCF:
        pass
    elif getattr(LispFunctions, "SETQ") == LispFunctions.SETQ:
        pass
    elif getattr(LispFunctions, "INPUT") == LispFunctions.INPUT:
        pass
    elif getattr(LispFunctions, "READ") == LispFunctions.READ:
        pass
    elif getattr(LispFunctions, "PRINT") == LispFunctions.PRINT:
        pass
    elif getattr(LispFunctions, "LOOP") == LispFunctions.LOOP:
        pass
    elif getattr(LispFunctions, "IF") == LispFunctions.IF:
        pass
    elif getattr(LispFunctions, "RETURN") == LispFunctions.RETURN:
        pass
    elif getattr(LispFunctions, "MOD") == LispFunctions.MOD:
        pass
    elif getattr(LispFunctions, "ZEROP") == LispFunctions.ZEROP:
        pass
    elif getattr(LispFunctions, "PLUS") == LispFunctions.PLUS:
        pass
    elif getattr(LispFunctions, "MINUS") == LispFunctions.MINUS:
        pass
    elif getattr(LispFunctions, "MUL") == LispFunctions.MUL:
        pass
    elif getattr(LispFunctions, "DIV") == LispFunctions.DIV:
        pass
    elif getattr(LispFunctions, "GR") == LispFunctions.GR:
        pass
    elif getattr(LispFunctions, "LE") == LispFunctions.LE:
        pass
    elif getattr(LispFunctions, "EQ") == LispFunctions.EQ:
        pass
    elif getattr(LispFunctions, "LOE") == LispFunctions.LOE:
        pass
    elif getattr(LispFunctions, "GOE") == LispFunctions.GOE:
        pass
    elif getattr(LispFunctions, "FORMAT") == LispFunctions.FORMAT:
        pass
    elif getattr(LispFunctions, "TERPRI") == LispFunctions.TERPRI:
        pass


def translate(source):
    source = preprocess(source)
    res = lisp_to_s_expr(source)
    return res

def main(source, target):
    f = open(source, "r")
    source = f.read()
    s_exps = translate(source)
    print(s_exps)

if __name__ == "__main__":
    assert len(sys.argv) == 3, "Correct use of translator: translation.py <source_file> <output_file>"
    name, source, target = sys.argv
    main(source, target)