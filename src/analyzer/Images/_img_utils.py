from PIL import Image


def get_resolution_image(path):
    try:
        return Image.open(path).size
    except:
        print(f"An error occured reading image {path}")
        return (-1, -1)
