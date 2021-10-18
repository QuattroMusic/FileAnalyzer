""""
General infos
File size, amount, average size, extension, on the bottom, the total of all

Images
size, extension, amount

Audios
size, mean duration, extension, amount

Videos
size, duration, extension, amount

Programming Languages
Rows: amount, empty, non-empty, import, commented
characters, numbers, whitespaces (1 tab = 1 enter = 1 space = 1)
Language

TODO add a final row with the total (sum of all rows)
"""
import generic
from prettytable.prettytable import PrettyTable
from os import listdir
from os.path import isfile, join
from pkgutil import iter_modules
from ProgrammingLanguages import _function_utils as utils

modules = [name for _, name, _ in iter_modules(['ProgrammingLanguages'])]

for mod in modules:
    exec(f"import ProgrammingLanguages.{mod} as {mod}_analyzer")

#path = input("Insert the path of the folder/file: ")

path = "../"

response = ""
allFiles = []
data = []

def get_files(path, continuous=""):
    # recursive algorythm to get all the files
    # also enters folders
    path += f"{continuous}/"
    try:
        for f in listdir(path):
            if isfile(join(path, f)):
                allFiles.append(path + f)
            else:
                get_files(path, f)
    except:
        allFiles.append(path)

# start getting all the files and stores them in an array
get_files(path)

# analyzing the data
for filePath in allFiles:
    ext = utils.get_extension(filePath)
    for mod in modules:
        if mod == "_function_utils" or mod == "__init__": continue
        
        exec(f"response = {mod}_analyzer.should_analyze(\"{ext}\")")
        if(response):
            exec(f"{mod}_analyzer.analyze('{filePath}')")
            break
    generic.analyze(filePath)
# visualizing data
genericTable = PrettyTable()
programmingLanguageTable = PrettyTable()
charactersLanguageTable = PrettyTable()

programmingLanguageTable.field_names = ["Language", "Extension",
                                        "Rows Count", "Non-Empty Rows", "Empty Rows", "Commented Rows", "Imported Rows"]
charactersLanguageTable.field_names = [
    "Language", "Letters", "Symbols", "White Spaces", "Digits", "Numbers", "Total"]

row_total = [0] * 7
char_total = [0] * 7
for mod in modules:
    if mod == "_function_utils" or mod == "__init__": continue
    
    exec(f"data = {mod}_analyzer.get_data()")
    
    if len(data) != 0:
        row_dict, char_dict = data
        
        row_data = []
        row_data.append(row_dict["lang"])
        row_data.append(row_dict["extension"])
        row_data.append(row_dict["rows"])
        row_data.append(row_dict["non_empty_rows"])
        row_data.append(row_dict["empty_rows"])
        row_data.append(row_dict["comment_rows"])
        row_data.append(row_dict["import_rows"])
        
        
        char_data = []
        char_data.append(char_dict["lang"])
        char_data.append(char_dict["letters"])
        char_data.append(char_dict["symbols"])
        char_data.append(char_dict["whitespaces"])
        char_data.append(char_dict["digits"])
        char_data.append(char_dict["numbers"])
        char_data.append(char_dict["total"])
        
        for i, numb in enumerate(row_data):
            if type(numb) is str: continue
            row_total[i] += numb
        for i, numb in enumerate(char_data):
            if type(numb) is str: continue
            char_total[i] += numb
        
        programmingLanguageTable.add_row(row_data)
        charactersLanguageTable.add_row(char_data)

#TODO: if file type is just one, there is no reason to show "any"

row_total[0] = "Any"
row_total[1] = "*"
char_total[0] = "Any"

programmingLanguageTable.add_row(row_total)
charactersLanguageTable.add_row(char_total)

for ih,oh in zip(generic.get_data(), ["Extension", "File Count", "Min Weight", "Max Weight", "Average Weight", "Total Weight"]):
    genericTable.add_column(oh,ih)

print(genericTable)
print()
print(programmingLanguageTable)
print()
print(charactersLanguageTable)
