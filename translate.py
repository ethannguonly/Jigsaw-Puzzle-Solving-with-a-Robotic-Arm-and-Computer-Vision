import cv2
import numpy as np
from PIL import Image

im = Image.open('piece1.png')
pix = im.load()
width, height = im.size
for x in range(0, width):
    for y in range(0, height):
        if pix[x, y]==(255, 255, 255):
            pix[x, y]=(0, 0, 0)
        else:
            pix[x, y]=(255, 255, 255)
im.save('piece1translated.png')
img = cv2.imread('piece1translated.png',0)
rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))
img = Image.fromarray(dst)
img.save('piece1translated.png')
im = Image.open('piece1translated.png')
pix = im.load()
for x in range(0, width):
    for y in range(0, height):
        if pix[x, y]==0:
            pix[x, y]=255
        else:
            pix[x, y]=0
im.save('piece1translated.png')