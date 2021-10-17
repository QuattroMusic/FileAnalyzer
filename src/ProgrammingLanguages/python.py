from . import _function_utils as fu
from re import split as re_split

# file amount, rows, non-empty rows, empty rows, commented rows, imported rows
# letters, symbols, whitespaces, digits, numbers, total
rowsData = ["Python", ".py", 0, 0, 0, 0, 0, 0]
charactersData = ["Python", 0, 0, 0, 0, 0, 0]


def should_analyze(ext):
    return ext in [".py", ".pyw"]


def analyze(path):
    print(path)
    file = fu.get_file_content(path)

    # Rows Data
    # +1 file, +rows amt
    rowsData[2] += 1
    rowAmt = fu.get_row_amount(file)
    rowsData[3] += rowAmt

    # empty and non-empty rows
    for row in file.split("\n"):
        if len(row) == 0:
            # empty
            rowsData[5] += 1
        else:
            # non-empty
            rowsData[4] += 1
    # comment and import

    for row in file.split("\n"):
        row = row.replace(" ", "")
        print(row)
        # far finire nella stessa riga e controllare se non è una variabile
        # TODO: comments at the end of the line aren't being counted
        if row[0:1] == "#":
            # commented
            rowsData[6] += 1
        elif row[0:4] == "from" or row[0:6] == "import":
            # imports
            rowsData[7] += 1

    # Characters Data
    for row in fu.get_file_raw_content(path):
        numbersSplit = re_split('(\d+\.?\d*)', row)
        if len(numbersSplit) != 1:
            charactersData[5] += len(numbersSplit) // 2
        for char in row:
            if char.isalpha():
                charactersData[1] += 1
            elif char in [" ", "	"]:
                # one is space, the other is \t
                charactersData[3] += 1
            elif char in [i for i in "1234567890"]:
                charactersData[4] += 1
            else:
                if char != "\n":
                    # symbols
                    charactersData[2] += 1
    # counts the final \n as whitespace
    charactersData[3] += (rowAmt - 1)

    # total
    charactersData[-1] = sum(charactersData[1:-1])

    print(rowsData)


def get_data():
    return rowsData, charactersData
