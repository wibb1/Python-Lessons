def replace_last(string, delimiter, replacement):
    start, _, end = string.rpartition(delimiter)
    return start + replacement + end