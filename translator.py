import sys

from preprocessor import preprocess

data_labels = {}
code_labels = {}

def findDataSection(lines):
    for i in range(0, len(lines)):
        if "section .data" in lines[i]:
            return i
    return 0

def findCodeSection(lines):
    for i in range(0, len(lines)):
        if "section .text" in lines[i]:
            return i
    return 0

def translateData(lines, start_idx, end_idx):
    for line in lines[start_idx:end_idx]:
        instrs = line.split(' ')


def translateCode(lines, start_idx, end_idx):
    for line in lines[start_idx:end_idx]:
        instrs = line.split(' ')

def translate(source):
    lines = source.split(' ')

    data_start = findDataSection(lines)
    code_start = findCodeSection(lines)

    translated_data = ''
    translate_code = ''

    if data_start == code_start == 0:
        print("No '.data' and '.code' section. Terminated.")
        exit(1)

    elif code_start == 0:
        print("No '.text' section. Terminated.")
        exit(1)

    elif data_start > code_start:
        translated_data = translateData(lines, data_start, len(lines))
        translate_code = translateCode(lines, code_start, data_start)
    else:
        translated_data = translated_data(lines, data_start, code_start)
        translate_code = translateCode(lines, code_start, len(lines))




def main(source, target):
    fr = open(source, "r")
    source_str = fr.read()
    fr.close()
    preprocessed = preprocess(source_str)

    fw = open(target, "w")
    fw.write(preprocessed)
    fw.close()

if __name__ == "__main__":
    assert len(sys.argv) == 3, "Correct use of translator: translation.py <source_file> <output_file>"
    name, source, target = sys.argv
    main(source, target)