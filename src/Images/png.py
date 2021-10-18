#import _function_utils as utils
from re import split as re_split

# rows, non-empty rows, empty rows, commented rows, imported rows
# letters, symbols, whitespaces, digits, numbers, total
rowsData = {
    "type": "PNG",
    "extension": ".png",
    "file_count": 0,
    "min_resolution": 0,
    "max_resolution": 0,
    "average_resolution": 0
}

def should_analyze(ext):
    return ext in [".png"]

def analyze(path):
    pass

def get_data():
    return rowsData