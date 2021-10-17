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
import Generic
from prettytable.prettytable import PrettyTable
from os import listdir
from os.path import isfile, join
from pkgutil import iter_modules
import FunctionUtil as fu

modules = [name for _, name, _ in iter_modules(['FileAnalyzer/ProgrammingLanguages'])]

for mod in modules:
    exec(f"import ProgrammingLanguages.{mod} as {mod}Executer")

#path = input("Insert the path of the folder/file: ")

path = "D:/Projects/GitHubProjects/2021/FileAnalyzer/"

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
    ext = fu.get_extension(filePath)
    for mod in modules:
        exec(f"response = {mod}Executer.should_analyze(\"{ext}\")")
        if(response):
            exec(f"{mod}Executer.analyze('{filePath}')")
            break
    Generic.analyze(filePath)
# visualizing data
genericTable = PrettyTable()
programmingLanguageTable = PrettyTable()
charactersLanguageTable = PrettyTable()

programmingLanguageTable.field_names = ["Language", "Extension", "File Amount",
                                        "Rows Count", "Non-Empty Rows", "Empty Rows", "Commented Rows", "Imported Rows"]
charactersLanguageTable.field_names = [
    "Language", "Letters", "Symbols", "White Spaces", "Digits", "Numbers", "Total"]

for mod in modules:
    exec(f"data = {mod}Executer.get_data()")
    if len(data) != 0:
        programmingLanguageTable.add_row(data[0])
        charactersLanguageTable.add_row(data[1])

genericTable.add_row(Generic.get_data())

print(genericTable)
print()
print(programmingLanguageTable)
print()
print(charactersLanguageTable)
