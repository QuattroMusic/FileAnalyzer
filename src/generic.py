from os import stat
from typing import List, Dict, Union

from . import utils

extensionData = []
fileAmountData = []
min_weight = []
max_weight = []
average_weight = []
total_weights = []

weights: Dict[ str, List[ Union[str, int] ] ] = {}
sizes = ["byte", "Kb", "Mb", "Gb", "Tb"]


def process_size(size):
    index = 0
    while size >= 1024 and index <= 3:
        size /= 1024
        index += 1
    if sizes[index] == "byte":
        return f"{round(size)} byte"
    return f"{round(size, 2)} {sizes[index]}"


def analyze(path):
    ext = utils.get_extension(path)
    if ext is None:
        return
    # append extension
    if ext not in extensionData:
        extensionData.append(ext)
        fileAmountData.append(1)
    else:
        fileAmountData[ extensionData.index(ext) ] += 1

    # creates a list of lists
    # every sub-list contains the files with the same extension
    # [[.py,.py],[.r,.r]]
    for extW in weights:
        if extW == ext:
            weights[ext].append(path)
            break
    else:
        weights[ext] = [path]


def get_data():
    # remove the useless infos (like the extensions and the [None])
    # the extension is useless because the array is sorted based on the others array
    # replace the paths in the array with his respective weight in bytes
    for ext in weights:
        for index, obj in enumerate( weights[ext] ):
            weights[ext][index] = stat( weights[ext][index] ).st_size

    for value in weights.values():
        # calculate the respective min, max, average and total
        min_weight.append( process_size( min(value) ) )
        max_weight.append( process_size( max(value) ) )
        average_weight.append( process_size( sum(value) / len(value) ) )
        total_weights.append( process_size( sum(value) ) )

    #TODO: add the total at the bottom

    listona = list( zip( extensionData, fileAmountData, min_weight, max_weight, average_weight, total_weights ) )

    listona.sort( key=lambda x: x[1], reverse=True )

    return listona
