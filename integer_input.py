import re


def input_integer(some_input):
    regex = r'[-+]?\d+'
    if re.fullmatch(regex, some_input):
        result = True
    else:
        result = False

    return result
