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
    "lang": "Python",
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
    pass


def analyze_chars(file: str):
    pass


def get_data():
    return rowsData, charactersData
