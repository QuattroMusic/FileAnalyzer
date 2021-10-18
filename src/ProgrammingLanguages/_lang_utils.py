from typing import Tuple

def get_file_content(path: str):
    with open(path, "r") as f:
        return f.read()

def get_file_raw_content(path: str):
    with open(path, "r") as f:
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
