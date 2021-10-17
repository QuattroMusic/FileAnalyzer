from os import stat
from ProgrammingLanguages import _function_utils as utils

extensionData = []
fileAmountData = []

#print(stat("main.py").st_size)

def analyze(path):
    ext = utils.get_extension(path)
    if ext is None: return
    #TODO: add the file name (.py -> Python, ...)
    #append extension
    if ext not in extensionData:
        extensionData.append(ext)
        fileAmountData.append(1)
    else:
        fileAmountData[extensionData.index(ext)] += 1

    #TODO: il resto

def get_data():
    return extensionData, fileAmountData
