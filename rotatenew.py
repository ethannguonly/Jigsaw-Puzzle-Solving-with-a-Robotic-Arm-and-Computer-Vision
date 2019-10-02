import cv2
from PIL import Image

def rotateImage(image, angle):
  image_center = tuple([452, 562])
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

im = Image.open('piece1.png')
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
img = rotateImage(img, 90)
im2 = Image.fromarray(img)
im2.save('rotated.png')
im3 = Image.open('rotated.png')
pix = im3.load()
for x in range(0, width):
    for y in range(0, height):
        if pix[x, y]==(0, 0, 0):
            pix[x, y]=(255, 255, 255)
        else:
            pix[x, y]=(0, 0, 0)
im3.save('rotated.png')