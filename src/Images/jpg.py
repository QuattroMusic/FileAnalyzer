from ._img_utils import get_resolution_image

rowsData = {
    "type": "JPG",
    "extension": ".jpg",
    "file_count": 0,
    "min_resolution": "",
    "max_resolution": "",
}
resolutions = []
resolutionsProduct = []

def should_analyze(ext):
    return ext in [".jpg"]

def analyze(path):
    width, height = get_resolution_image(path)
    if width == -1 and height == -1:
        return
    resolutions.append([width,height])
    resolutionsProduct.append(width*height)

    rowsData["file_count"] += 1
    minRes = resolutions[resolutionsProduct.index(min(resolutionsProduct))]
    maxRes = resolutions[resolutionsProduct.index(max(resolutionsProduct))]
    rowsData["min_resolution"] = f"{minRes[0]} x {minRes[1]}"
    rowsData["max_resolution"] = f"{maxRes[0]} x {maxRes[1]}"

def get_data():
    return rowsData