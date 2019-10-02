from PIL import Image

if __name__=="__main__":
    im = Image.open('frozenblack.jpg') # Can be many different formats.
    pix = im.load()
    print(im.size)  # Get the width and hight of the image for iterating over
    width, height = im.size
    background={}
    for x in range(0, width):
        for y in range(0, height):
            if pix[x, y][0]>132 and pix[x, y][1]>132 and pix[x, y][2]>132:
                pix[x, y]=(255, 255, 255)
    im.save('frozen.png')  # Save the modified pixels as .png