#!/usr/bin/python
from PIL import Image
import os, sys
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

path = "screenshots/"
dirs = os.listdir( path )


def crop():
    for item in dirs:
        fullpath = os.path.join(path,item)
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            f, e = os.path.splitext(fullpath)
            imCrop = im.crop((0, 0, 1366, 768))
            imCrop.save(f + 'cropped.png', "PNG", quality=100)

crop()