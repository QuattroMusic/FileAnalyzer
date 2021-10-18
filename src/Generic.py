from os import stat
from ProgrammingLanguages import _function_utils as utils

extensionData = []
fileAmountData = []
min_weight = []
max_weight = []
average_weight = []
total_weights = []

weights = [[None]]
sizes = ["byte", "Kb", "Mb", "Gb", "Tb"]

def process_size(size):
    index = 0
    while size >= 1024 and index<=3:
        size /= 1024
        index += 1
    return f"{round(size,2)} {sizes[index]}"

def analyze(path):
    ext = utils.get_extension(path)
    if ext is None: return
    #append extension
    if ext not in extensionData:
        extensionData.append(ext)
        fileAmountData.append(1)
    else:
        fileAmountData[extensionData.index(ext)] += 1

    # creates a list of lists
    # every sub-list contains the files with the same extension
    # [[.py,.py],[.r,.r]]
    for i in range(len(weights)):
        if weights[i][0] == ext:
            weights[i].append(path)
            break
    else:
        weights.append([ext, path])

def get_data():
    # remove the useless infos (like the extensions and the [None])
    # the extension is useless because the array is sorted based on the others array
    # replace the paths in the array with his respective weight in bytes
    weights.pop(0)
    for i in range(len(weights)):
        weights[i].pop(0)
        for index,obj in enumerate(weights[i]):
            weights[i][index] = stat(weights[i][index]).st_size

    for i in weights:
        # calculate the respective min, max, average and total
        min_weight.append(process_size(min(i)))
        max_weight.append(process_size(max(i)))
        average_weight.append(process_size(sum(i)/len(i)))
        total_weights.append(process_size(sum(i)))

    #TODO: add the total at the bottom
    return extensionData, fileAmountData, min_weight, max_weight, average_weight, total_weights
