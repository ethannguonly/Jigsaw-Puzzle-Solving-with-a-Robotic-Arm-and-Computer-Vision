from PIL import Image
import cv2
import numpy as np

GREEN_RANGE_MIN_HSV = (100, 200, 70)
GREEN_RANGE_MAX_HSV = (185, 255, 255)

def rgb_to_hsv(r, g, b):
    """
        Convert a color from rgb space to hsv

        :param r: red composant of rgb color
        :param g: green composant of rgb color
        :param b: blue composant of rgb color
        :return: h, s, v composants
    """

    maxc = max(r, g, b)
    minc = min(r, g, b)
    v = maxc
    if minc == maxc:
        return 0.0, 0.0, v
    s = (maxc-minc) / maxc
    rc = (maxc-r) / (maxc-minc)
    gc = (maxc-g) / (maxc-minc)
    bc = (maxc-b) / (maxc-minc)
    if r == maxc:
        h = bc-gc
    elif g == maxc:
        h = 2.0+rc-bc
    else:
        h = 4.0+gc-rc
    h = (h/6.0) % 1.0
    return h, s, v

def remove_background(path, factor=0.84):
    """
        Remove the green background of the image and save it

        :param path: path of the image to load
        :param factor: factor used to determine the interval of saturation to use
        :return: Nothing
    """

    print("Try remove background with factor ", factor)
    
    # Load image and convert it to RGBA, so it contains alpha channel
    im = Image.open(path)
    im = im.convert('RGBA')

    # Go through all pixels and turn each 'green' pixel to transparent
    pix = im.load()
    width, height = im.size
    mean_s = []
    for x in range(width):
        for y in range(height):
            r, g, b, a = pix[x, y]
            if g > r+70 and g > b+90:
                pix[x, y] = (0, 0, 0)
            else:
                pix[x, y] = (255, 255, 255)

    im.save('./images/output/green_background_removed.png')