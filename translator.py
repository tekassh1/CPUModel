import sys, re

def remove_extra_spaces(source_lines):
    for line in source_lines:
        line = re.sub(r'\s+', ' ', line)

def remove_single_line_comments(source_lines):
    for line in source_lines:
        line = line[0 : line.find(';')]

def remove_multi_line_comments(source_lines):
    # for line in source_lines:
    #     line = line[0 : line.find(';')]

def remove_empty_lines(source_lines):


def preprocess(source):
    lines = source.splitlines()

    for line in lines:



def translate(source):

    return

def main(source, target):
    f = open(sys.argv[0], "r")
    source = f.read()
    machine_code = translate(source)
    write_machine_code(target)

if __name__ == "__main__":
    assert len(sys.argv) == 3, "Correct use of translator: translation.py <source_file> <output_file>"
    name, source, target = sys.argv
    main(source, target)