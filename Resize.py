#!/usr/bin/python
from PIL import Image
import os, sys

path = "C:\\Users\\Ryan's Desktop\\PycharmProjects\\Learning\\images\\"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((68, 68), Image.ANTIALIAS)
            imResize.save(f.lower() + '.png', 'PNG')

resize()

