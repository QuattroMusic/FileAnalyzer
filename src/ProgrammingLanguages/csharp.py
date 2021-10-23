from . import _lang_utils as utils
from re import split as re_split

rowsData = {
    "lang": "CSharp",
    "extension": ".cs",
    "rows": 0,
    "non_empty_rows": 0,
    "empty_rows": 0,
    "comment_rows": 0,
    "import_rows": 0
}
charactersData = {
    "lang": "CSharp",
    "letters": 0,
    "symbols": 0,
    "whitespaces": 0,
    "digits": 0,
    "numbers": 0,
    "total": 0
}


def reset():
    for key, value in rowsData.items():
        print(key, value)
        if type(value) is int:
            rowsData[key] = 0
    for key, value in charactersData.items():
        if type(value) is int:
            charactersData[key] = 0


def should_analyze(ext):
    return ext in [".cs"]


def analyze(path):
    file = utils.get_file_content(path)
    analyze_rows(file)
    analyze_chars(file)


def analyze_rows(file):
    
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

        stripped = row.strip()
        if len(stripped) > 0 and stripped.startswith("//"):
            # commented
            rowsData["comment_rows"] += 1
        elif len(stripped) > 0:
            # check if there's a comment in the middle of the line
            # comment must not be inside a standard string
            
            # when you split based on string rows, you can either be inside the string, or outside
            # pieces outside the string are in the odd positions, pieces inside in the evens
            splitted = [piece for i, piece in enumerate(stripped.split("\"")) if i % 2 == 0]
            
            # search for comments in each code part not in strings
            for piece in splitted:
                if '//' in piece:
                    rowsData["comment_rows"] += 1
                    break # when you've found a comment symbol, the rest of the line is a comment, don't count it again
        
        
        if row.startswith("using"):
            # imports
            rowsData["import_rows"] += 1


def analyze_chars(file: str):
    rows = file.splitlines(True)
    rowAmt = utils.get_row_amount(file)
    
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



def get_data():
    return rowsData, charactersData
