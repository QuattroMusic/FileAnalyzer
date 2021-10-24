from re import search
from pathlib import Path
from typing import List, Optional


def get_files(path: Path) -> List[Path]:
    # recursive algorythm to get all the files
    # also enters folders
    files: List[Path] = []
    for obj in path.glob('*'):
        if obj.name.startswith('_'):
            continue
        if obj.is_file():
            files.append(obj)
        else:
            files += get_files(obj)
    return files


def get_extension(path: Path) -> Optional[str]:
    if path.name.find('.') == -1:
        return None
    else:
        return path.name[ path.name.find('.'): ]


def number_format(num: float, char: str = "˙"):
    """
    Function that add the symbol ˙ every 3 digits if 'char' argument is none
    If the char argument is given, it will place the given symbol
    """
    num_str = str( abs(num) )
    fin = ""
    try:
        if num_str[1] == "e":
            return num
    except IndexError:
        return num
    try:
        num_intpart = num_str[0:search('\.', num_str).start()]
    except IndexError:
        num_intpart = num_str
    for i in range(len(num_intpart)):
        k = abs(i - len(num_intpart))
        fin += num_intpart[i]
        if k % 3 == 1:
            fin += char
    try:
        if num > 0:
            return fin[0:-1] + num_str[ (search(r'\.', num_str).start() ): ]
        else:
            return "-" + fin[0:-1] + num_str[ (search(r'\.', num_str).start() ): ]
    except IndexError:
        if num > 0:
            return fin[0:-1]
        else:
            return "-" + fin[0:-1]
