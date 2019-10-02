from PIL import Image

if __name__=="__main__":
    im = Image.open('frozen3.png') # Can be many different formats.
    pix = im.load()
    print(im.size)  # Get the width and hight of the image for iterating over
    width, height = im.size
    background={}
    for x in range(0, width):
        for y in range(0, height):
            if pix[x, y]==(0, 0, 0):
                pix[x, y]=(255, 255, 255)
    # for x in range(0, width):
    #     for y in range(0, height):
    #         if pix[x, y]!=(255, 255,255):
    #             pix[x, y]=(0, 0, 255)
    im.save('frozen4.png')  # Save the modified pixels as .png
