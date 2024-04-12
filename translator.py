import re
import sys

from isa import functions, Instruction
from preprocessor import preprocess


def split_string_with_quotes(s):
    parts = re.findall(r'"[^"]*"|[^\s]+', s)
    return parts

def parse_lisp(source):
    source = source.strip()
    assert source[0] == '(' and source[-1] == ')', "Wrong brackets sequence"

    source = source[1: -1]
    if source == '':
        return Instruction(None, None)

    # Recursion endpoint - No brackets
    if not (('(' in source) or (')' in source)):
        terms = split_string_with_quotes(source)

        if len(terms) == 1:                                                                        # (val) case
            if terms[0] in functions:
                return Instruction(terms[0], None)
            else:
                return terms[0]
        elif len(terms) == 2:                                                                      # (var value) case
            if terms[0] in functions:
                return Instruction(terms[0], [terms[1]])
            return Instruction('', terms)

        assert (terms[0] in functions) or terms[0] == '',  f'Function {terms[0]} doesn\'t exist'   # (op arg1 arg2) case
        return Instruction(terms[0], terms[1: len(terms)])

    # Resolve args
    is_started = False

    start_idx = 0
    end_idx = 0
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
                end_idx = i
                is_started = False
                if len(args) == 0:
                    opcode = source[0:start_idx].strip()
                    assert opcode in functions or opcode == '', f'Function {opcode} doesn\'t exist'

                args.append(parse_lisp(source[start_idx: end_idx + 1]))

        assert cntr >= 0, "Wrong code format (missed brackets)"

    assert cntr == 0, "Wrong code format (extra brackets)"
    return Instruction(opcode, args)

def translate(source):
    source = preprocess(source)
    res = parse_lisp(source)
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