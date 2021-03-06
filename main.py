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
from argparse import ArgumentParser
from pathlib import Path
from typing import Tuple, cast, Union, Dict

import src.generic
import src.analyzer
from prettytable.prettytable import PrettyTable
import sys
from src import utils

src.analyzer.init_analyzers()


class Arguments:
    directory: Path


parser = ArgumentParser(
    prog='',
    description=''
)
parser.add_argument(
    'directory',
    default=Path('.'),
    help='Directory to search in',
    type=Path,
    nargs='?'
)
args: Arguments = cast( Arguments, parser.parse_args( sys.argv[1:] ) )


if not args.directory.exists():
    print("This path does not exists")
    exit()


# start getting all the files and stores them in an array
# analyzing the data
for filePath in utils.get_files(args.directory):
    ext = utils.get_extension(filePath)

    analyzer = src.analyzer.get_compatible_analyzer(ext)
    if analyzer is not None:
        analyzer.analyze( str( filePath ) )

    src.generic.analyze(filePath)

# visualizing data
genericTable = PrettyTable()
programmingLanguageTable = PrettyTable()
charactersLanguageTable = PrettyTable()
imagesTable = PrettyTable()
audiosTable = PrettyTable()

genericTable.field_names = [
    "Extension",
    "File Count",
    "Min Weight",
    "Max Weight",
    "Average Weight",
    "Total Weight"
]
programmingLanguageTable.field_names = [
    "Language",
    "Extension",
    "Rows Count",
    "Non-Empty Rows",
    "Empty Rows",
    "Commented Rows",
    "Imported Rows"
]
charactersLanguageTable.field_names = [
    "Language",
    "Letters",
    "Symbols",
    "White Spaces",
    "Digits",
    "Numbers",
    "Total"
]
imagesTable.field_names = [
    "Type",
    "Extension",
    "File Count",
    "Min Resolution",
    "Max Resolution"
]
audiosTable.field_names = [
    "Type",
    "Extension",
    "File Count",
    "Min Duration",
    "Max Duration"
]


row_total: Dict[str, Union[str, int] ] = {
    'lang': 'Any',
    'extension': '.*',
    'rows': 0,
    'non_empty_rows': 0,
    'empty_rows': 0,
    'comment_rows': 0,
    'import_rows': 0
}
char_total: Dict[str, Union[str, int] ] = {
    'lang': 'Any',
    'letters': 0,
    'symbols': 0,
    'whitespaces': 0,
    'digits': 0,
    'numbers': 0,
    'total': 0
}
row_count = 0


for mod in src.analyzer.get_analyzers_for_package('ProgrammingLanguages'):

    data: Tuple[dict, dict] = mod.get_data()

    if len(data) != 0:
        row_dict, char_dict = data

        programmingLanguageTable.add_row( row_dict.values() )
        charactersLanguageTable.add_row( char_dict.values() )

        for key in row_dict:
            if key not in ('lang', 'extension'):
                row_total[ key ] += row_dict[ key ]

        for key in char_dict:
            if key not in ('lang', 'extension'):
                char_total[ key ] += char_dict[ key ]

        row_count += 1


showImageTable = False
for mod in src.analyzer.get_analyzers_for_package('Images'):

    data: dict = mod.get_data()

    if data["min_resolution"] != "":
        imagesTable.add_row( data.values() )
        showImageTable = True


showAudioTable = False
for mod in src.analyzer.get_analyzers_for_package('Audios'):
    data: dict = mod.get_data()

    if data["min_duration"] != "":
        audiosTable.add_row( data.values() )
        showAudioTable = True


if row_count > 1:
    programmingLanguageTable.add_row( row_total.values() )
    charactersLanguageTable.add_row( char_total.values() )

for i in src.generic.get_data():
    genericTable.add_row(i)

print(genericTable, '\n')
print(programmingLanguageTable, '\n')
print(charactersLanguageTable, '\n')

if showImageTable:
    print(imagesTable, '\n')

if showAudioTable:
    print(audiosTable, '\n')
