import PIL.Image

rowsData = {
    "type": "PNG",
    "extension": ".png",
    "file_count": 0,
    "min_resolution": "",
    "max_resolution": "",
}
resolutions = []
resolutionsProduct = []

def should_analyze(ext):
    return ext in [".png"]

def analyze(path):
    width, height = PIL.Image.open(path).size
    resolutions.append([width,height])
    resolutionsProduct.append(width*height)

    rowsData["file_count"] += 1
    minRes = resolutions[resolutionsProduct.index(min(resolutionsProduct))]
    maxRes = resolutions[resolutionsProduct.index(max(resolutionsProduct))]
    rowsData["min_resolution"] = f"{minRes[0]} x {minRes[1]}"
    rowsData["max_resolution"] = f"{maxRes[0]} x {maxRes[1]}"

def get_data():
    return rowsData