import re

def remove_comments(source):
    lines = source.split('\n')
    cleaned_source = []
    for line in lines:
        line = re.sub(r';.*$', '', line)
        cleaned_source.append(line)

    cleaned_text = '\n'.join(cleaned_source)
    return cleaned_text

def remove_extra_spaces(source):
    lines = source.split('\n')
    cleaned_source = []
    for line in lines:
        line = line.strip()
        line = ' '.join(line.split())
        cleaned_source.append(line)

    cleaned_text = '\n'.join(cleaned_source)
    return cleaned_text

def remove_empty_strings(source):
    lines = source.split('\n')
    cleaned_source = []
    for line in lines:
        if line != "":
            cleaned_source.append(line)

    cleaned_text = '\n'.join(cleaned_source)
    return cleaned_text

def preprocess(source):
    source = remove_comments(source)
    source = remove_extra_spaces(source)
    source = remove_empty_strings(source)
    return source
