from PIL import Image
from skimage import io, img_as_float
import matplotlib.pyplot as plt
import numpy as np
from resizeimage import resizeimage

def resize_image(input_image_path,
                 output_image_path,
                 size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))

    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print('The resized image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
    resized_image.save(output_image_path)

if __name__=="__main__":
    # im = Image.open('frozenblack.jpg') # Can be many different formats.
    # pix = im.load()
    # print(im.size)  # Get the width and hight of the image for iterating over
    # width, height = im.size
    # background={}
    # for x in range(0, width):
    #     for y in range(0, height):
    #         if pix[x, y][0]<130 and pix[x, y][1]<130 and pix[x, y][2]<130:
    #             pix[x, y]=(255, 255, 255)
    # for x in range(width-70, width):
    #     for y in range(0, height):
    #         pix[x, y]=(255, 255, 255)
    # im.save('frozen.png')  # Save the modified pixels as .pngr
    #
    # for k in range(1, 5):
    #     im = Image.open('frozen.png')
    #     pix = im.load()
    #     if k!=1:
    #         for x in range(0, int(width/2)):
    #             for y in range(0, int(height/2)):
    #                 pix[x, y]=(255, 255, 255)
    #     if k!=2:
    #         for x in range(int(width/2), width):
    #             for y in range(0, int(height/2)):
    #                 pix[x, y]=(255, 255, 255)
    #     if k!=3:
    #         for x in range(0, int(width/2)):
    #             for y in range(int(height/2), height):
    #                 pix[x, y]=(255, 255, 255)
    #     if k!=4:
    #         for x in range(int(width/2), width):
    #             for y in range(int(height/2), height):
    #                 pix[x, y]=(255, 255, 255)
    #     im.save('piece'+str(k)+'.png')

    image = img_as_float(io.imread('piece1.png'))

    # Select all pixels almost equal to white
    # (almost, because there are some edge effects in jpegs
    # so the boundaries may not be exactly white)
    white = np.array([1, 1, 1])
    mask = np.abs(image - white).sum(axis=2) < 0.05

    # Find the bounding box of those pixels
    coords = np.array(np.nonzero(~mask))
    top_left = np.min(coords, axis=1)
    bottom_right = np.max(coords, axis=1)

    out = image[top_left[0]:bottom_right[0],
          top_left[1]:bottom_right[1]]

    plt.imsave("piece1cropped.png", out)

    img = Image.open('piece1cropped.png')
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save("piece1cropped2.png", "PNG")
    resize_image(input_image_path='piece1cropped2.png',
                 output_image_path='piece1cropped3.png',
                 size=(151, 219))