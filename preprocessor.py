import re

def remove_single_line_comments(source):
    return re.sub(r';.*\n', '\n', source)

def remove_multi_line_comments(source):
    return re.sub(r'\|#.*#\|', '', source)

def remove_newlines(source):
    return re.sub(r'\n', ' ', source)

def add_spaces_to_brackets(source):
    source = re.sub(r'\(', ' (', source)
    return re.sub(r'\)', ') ', source)

def remove_extra_spaces(source):
    return re.sub(r'\s+', ' ', source)

def preprocess(source):
    source = remove_single_line_comments(source)
    source = remove_multi_line_comments(source)
    source = remove_newlines(source)
    source = add_spaces_to_brackets(source)
    source = remove_extra_spaces(source)

    return source