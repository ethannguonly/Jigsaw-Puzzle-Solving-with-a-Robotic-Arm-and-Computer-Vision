import cv2
from PIL import Image
import scipy.misc

def rotate(piece, center, angle):
    im = Image.open(piece)
    pix = im.load()
    width, height = im.size
    for x in range(0, width):
        for y in range(0, height):
            if pix[x, y]==(255, 255, 255):
                pix[x, y]=(0, 0, 0)
            else:
                pix[x, y]=(255, 255, 255)
    im.save('rotated.png')
    img = cv2.imread('rotated.png',0)
    rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)
    img = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)
    scipy.misc.imsave('rotated.png', img)

    im = Image.open('rotated.png')
    pix = im.load()
    for x in range(0, width):
        for y in range(0, height):
            if pix[x, y]==0:
                pix[x, y]=255
            else:
                pix[x, y]=0
    im.save('rotated.png')