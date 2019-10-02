from PIL import Image
img = Image.open("./images/samples/flipped.jpg")
width, height = img.size
pix = img.load()
for x in range(0, 40):
    for y in range(0, height):
        pix[x, y]= (0, 255, 0)
        pix[width-x-1, y] = (0, 255, 0)
for y in range(0, 70):
    for x in range(0, width):
        pix[x, y]=(0, 255, 0)
for y in range(height-31, height):
    for x in range(0, width):
        pix[x, y] = (0, 255, 0)
for x in range(int(width/2)-200, int(width/2)+200):
    for y in range(1100, height):
        pix[x, y]= (0, 255, 0)
img.save("./images/samples/greenborder.jpg")