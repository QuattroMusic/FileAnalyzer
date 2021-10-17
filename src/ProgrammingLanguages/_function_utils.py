from re import search
from typing import Tuple

def get_file_content(path: str):
    with open(path, "r") as f:
        return f.read()


def get_file_raw_content(path: str):
    with open(path, "r") as f:
        return f.readlines()


def get_extension(path: str):
    extension = ""
    for i in range(len(path) - 1, -1, -1):
        extension += path[i]
        if path[i] == ".":
            break
    return extension[::-1]


def get_row_amount(file: str):
    return len(file.split("\n"))

def count_empty_or_not_rows(file: str) -> Tuple[int, int]:
    empty_rows = 0
    non_empty_rows = 0
    for row in file.split("\n"):
        if len(row) == 0:
            # empty
            empty_rows += 1
        else:
            # non-empty
            non_empty_rows += 1
    return (empty_rows, non_empty_rows)

def number_format(num: float, char: chr = "˙"):
    """
    Function that add the symbol ˙ every 3 digits if 'char' argument is none
    If the char argument is given, it will place the given symbol
    """
    num_str = str(abs(num))
    fin = ""
    try:
        if num_str[1] == "e":
            return num
    except:
        return num
    try:
        num_intpart = num_str[0:search('\.', num_str).start()]
    except:
        num_intpart = num_str
    for i in range(len(num_intpart)):
        k = abs(i - len(num_intpart))
        fin += num_intpart[i]
        if k % 3 == 1:
            fin += char
    try:
        if num > 0:
            return fin[0:-1] + num_str[(search('\.', num_str).start()):]
        else:
            return "-" + fin[0:-1] + num_str[(search('\.', num_str).start()):]
    except:
        if num > 0:
            return fin[0:-1]
        else:
            return "-" + fin[0:-1]
