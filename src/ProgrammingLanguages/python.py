from . import _function_utils as utils
from re import split as re_split

# rows, non-empty rows, empty rows, commented rows, imported rows
# letters, symbols, whitespaces, digits, numbers, total
rowsData = {
    "lang": "Python",
    "extension": ".py",
    "rows": 0,
    "non_empty_rows": 0,
    "empty_rows": 0,
    "comment_rows": 0,
    "import_rows": 0
}
charactersData = {
    "lang": "Python",
    "letters": 0,
    "symbols": 0,
    "whitespaces": 0,
    "digits": 0,
    "numbers": 0,
    "total": 0
}

def should_analyze(ext):
    return ext in [".py", ".pyw"]


def analyze(path):
    file = utils.get_file_content(path)

    # Rows Data
    rowAmt = utils.get_row_amount(file)
    rowsData["rows"] += rowAmt

    # empty and non-empty rows
    empty, non_empty = utils.count_empty_or_not_rows(file)
    rowsData["empty_rows"] += empty
    rowsData["non_empty_rows"] += non_empty

    # comment and import
    for row in file.split("\n"):
        row = row.replace(" ", "")

        # TODO: comments at the end of the line aren't being counted
        if row[0:1] == "#":
            # commented
            rowsData["comment_rows"] += 1
        elif row[0:4] == "from" or row[0:6] == "import":
            # imports
            rowsData["import_rows"] += 1

    # Characters Data
    for row in utils.get_file_raw_content(path):
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

def get_data():
    return rowsData, charactersData