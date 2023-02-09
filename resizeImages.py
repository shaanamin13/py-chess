import os
from PIL import Image


def resize_images():
    path = "images/"
    dirs = os.listdir(path)

    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((64, 64), Image.ANTIALIAS)
            imResize.save(f + '.jpg', 'JPEG', quality=90)


resize_images()
