from typing import Tuple
from re import split as re_split

def get_file_content(path: str):
    with open(path, "r", encoding='utf-8') as f:
        return f.read()

def get_file_raw_content(path: str):
    with open(path, "r", encoding='utf-8') as f:
        return f.readlines()

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

def analyze_chars(file: str, charactersData):
    rows = file.splitlines(True)
    rowAmt = get_row_amount(file)
    
    # Characters Data
    for row in rows:
        numbersSplit = re_split('(\d+\.?\d*)', row)
        if len(numbersSplit) != 1:
            charactersData["numbers"] += len(numbersSplit) // 2
        for char in row:
            if char.isalpha():
                charactersData["letters"] += 1
            elif char in [" ", "\t"]:
                # one is space, the other is \t
                charactersData["whitespaces"] += 1
            elif char.isnumeric():
                charactersData["digits"] += 1
            elif char != "\n":
                # symbols
                charactersData["symbols"] += 1
    
    # count the final \n of each row as whitespace
    charactersData["whitespaces"] += (rowAmt - 1)

    charactersData["total"] = charactersData["letters"] + charactersData["symbols"] + charactersData["whitespaces"] + charactersData["digits"]