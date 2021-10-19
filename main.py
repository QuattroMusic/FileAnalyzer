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
"""
import src.generic
from prettytable.prettytable import PrettyTable
from os import listdir
from os.path import isfile, join
from pkgutil import iter_modules
import src._function_utils as utils

langModules = [name for _, name, _ in iter_modules(["src/ProgrammingLanguages"])]
imgModules = [name for _, name, _ in iter_modules(["src/Images"])]

for mod in langModules:
    if mod[0] == "_": continue
    exec(f"import src.ProgrammingLanguages.{mod} as {mod}_analyzer")
for mod in imgModules:
    if mod[0] == "_": continue
    exec(f"import src.Images.{mod} as {mod}_analyzer")

#path = input("Insert the path of the folder/file: ")

path = "./"

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
    for mod in langModules + imgModules:
        if mod[0] == "_": continue
        exec(f"response = {mod}_analyzer.should_analyze(\"{ext}\")")
        if(response):
            exec(f"{mod}_analyzer.analyze('{filePath}')")
            break
    src.generic.analyze(filePath)
# visualizing data
genericTable = PrettyTable()
programmingLanguageTable = PrettyTable()
charactersLanguageTable = PrettyTable()
imagesTable = PrettyTable()

programmingLanguageTable.field_names = ["Language", "Extension",
                                        "Rows Count", "Non-Empty Rows", "Empty Rows", "Commented Rows", "Imported Rows"]
charactersLanguageTable.field_names = [
    "Language", "Letters", "Symbols", "White Spaces", "Digits", "Numbers", "Total"]
imagesTable.field_names = ["Type","Extension","File Count","Min Resolution","Max Resolution"]

row_total = [0] * 7
char_total = [0] * 7
row_count = 0
for mod in langModules:
    if mod[0] == "_": continue
    
    exec(f"data = {mod}_analyzer.get_data()")
    
    if len(data) != 0:
        row_dict, char_dict = data
        
        row_data = []
        char_data = []

        for i in row_dict:
            row_data.append(row_dict[i])
        for i in char_dict:
            char_data.append(char_dict[i])
        
        for i, numb in enumerate(row_data):
            if type(numb) is str: continue
            row_total[i] += numb
        for i, numb in enumerate(char_data):
            if type(numb) is str: continue
            char_total[i] += numb
        
        programmingLanguageTable.add_row(row_data)
        charactersLanguageTable.add_row(char_data)
        
        row_count += 1

for mod in imgModules:
    if mod[0] == "_": continue

    exec(f"data = {mod}_analyzer.get_data()")
    imgTableRow = []

    if len(data) != 0:
        for i in data:
            imgTableRow.append(data[i])
        imagesTable.add_row(imgTableRow)

row_total[0] = "Any"
row_total[1] = "*"
char_total[0] = "Any"

if row_count > 1:
    programmingLanguageTable.add_row(row_total)
    charactersLanguageTable.add_row(char_total)

for ih,oh in zip(src.generic.get_data(), ["Extension", "File Count", "Min Weight", "Max Weight", "Average Weight", "Total Weight"]):
    genericTable.add_column(oh,ih)

print(genericTable)
print()
print(programmingLanguageTable)
print()
print(charactersLanguageTable)
print()

if imgTableRow[2] != 0:
    print(imagesTable)
    print()
