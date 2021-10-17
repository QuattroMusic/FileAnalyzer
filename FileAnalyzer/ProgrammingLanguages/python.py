import FunctionUtil as fu
from re import split as reNumSplit

# file amount, rows, non-empty rows, empty rows, commented rows, imported rows
# letters, symbols, whitespaces, digits, numbers, total
rowsData = ["Python", ".py", 0, 0, 0, 0, 0, 0]
charactersData = ["Python", 0, 0, 0, 0, 0, 0]


def ShouldAnalyze(ext):
    return ext in [".py", ".pyw"]


def Analyze(path):
    file = fu.GetFileContent(path)

    multiLineComment = False

    # Rows Data
    # +1 file, +rows amt
    rowsData[2] += 1
    rowAmt = fu.GetRowAmount(file)
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
        # TODO: problemi con multiline comments """
        # far finire nella stessa riga e controllare se non è una variabile
        if multiLineComment:
            rowsData[6] += 1
            if row[0:3] == '"""':
                multiLineComment = False
                continue
        if row[0:3] == '"""':
            multiLineComment = not multiLineComment
            rowsData[6] += 1
        elif row[0:1] == "#":
            # commented
            rowsData[6] += 1
        elif row[0:4] == "from" or row[0:6] == "import":
            # imports
            rowsData[7] += 1

    # Characters Data
    for row in fu.GetFileRawContent(path):
        numbersSplit = reNumSplit('(\d+\.?\d*)', row)
        if len(numbersSplit) != 1:
            charactersData[5] += len(numbersSplit) // 2
        for char in row:
            if char in [i for i in "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"]:
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


def GetData():
    return rowsData, charactersData
