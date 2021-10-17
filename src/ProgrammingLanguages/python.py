from . import _function_utils as fu
from re import split as re_split

# file amount, rows, non-empty rows, empty rows, commented rows, imported rows
# letters, symbols, whitespaces, digits, numbers, total
rowsData = {
    "lang": "Python",
    "extension": ".py",
    "file_amount": 0,
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
    print(path)
    file = fu.get_file_content(path)

    # Rows Data
    # +1 file, +rows amt
    rowsData["file_amount"] += 1
    rowAmt = fu.get_row_amount(file)
    rowsData["rows"] += rowAmt

    # empty and non-empty rows
    for row in file.split("\n"):
        if len(row) == 0:
            # empty
            rowsData["empty_rows"] += 1
        else:
            # non-empty
            rowsData["non_empty_rows"] += 1
    # comment and import

    for row in file.split("\n"):
        row = row.replace(" ", "")
        print(row)
        # far finire nella stessa riga e controllare se non è una variabile
        # TODO: comments at the end of the line aren't being counted
        if row[0:1] == "#":
            # commented
            rowsData["comment_rows"] += 1
        elif row[0:4] == "from" or row[0:6] == "import":
            # imports
            rowsData["import_rows"] += 1

    # Characters Data
    for row in fu.get_file_raw_content(path):
        numbersSplit = re_split('(\d+\.?\d*)', row)
        if len(numbersSplit) != 1:
            charactersData["numbers"] += len(numbersSplit) // 2
        for char in row:
            if char.isalpha():
                charactersData["letters"] += 1
            elif char in [" ", "	"]:
                # one is space, the other is \t
                charactersData["whitespaces"] += 1
            elif char in [i for i in "1234567890"]:
                charactersData["digits"] += 1
            else:
                if char != "\n":
                    # symbols
                    charactersData["symbols"] += 1
    # counts the final \n as whitespace
    charactersData["whitespaces"] += (rowAmt - 1)

    # total
    charactersData["total"] = charactersData["letters"] + charactersData["symbols"] + charactersData["whitespaces"] + charactersData["digits"] + charactersData["numbers"]

    print(rowsData)


def get_data():
    # TODO: this is a temporary adaptor, you should return the dicts instead
    out_data = []
    out_data.append(rowsData["lang"])
    out_data.append(rowsData["extension"])
    out_data.append(rowsData["file_amount"])
    out_data.append(rowsData["rows"])
    out_data.append(rowsData["non_empty_rows"])
    out_data.append(rowsData["empty_rows"])
    out_data.append(rowsData["comment_rows"])
    out_data.append(rowsData["import_rows"])
    
    char_data = []
    char_data.append(charactersData["lang"])
    char_data.append(charactersData["letters"])
    char_data.append(charactersData["symbols"])
    char_data.append(charactersData["whitespaces"])
    char_data.append(charactersData["digits"])
    char_data.append(charactersData["numbers"])
    char_data.append(charactersData["total"])
    return out_data, char_data

def get_dict_data():
    return rowsData, charactersData