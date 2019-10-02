from PIL import Image
import cv2
import numpy as np

pieces = {}
corners = {}
edges = {}
interior = {}
def rotate(piece, center, angle):
    im = Image.open('piece'+str(piece)+'.png')
    pix = im.load()
    width, height = im.size
    for x in range(0, width):
        for y in range(0, height):
            if pix[x, y]==255:
                pix[x, y]=0
            else:
                pix[x, y]=255
    im.save('piece'+str(piece)+'.png')
    img = cv2.imread('piece'+str(piece)+'.png',0)
    rot_mat = cv2.getRotationMatrix2D(tuple(center), angle, 1.0)
    img = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)
    img2 = Image.fromarray(img)
    img2.save('piece'+str(piece)+'.png')

    im = Image.open('piece'+str(piece)+'.png')
    pix = im.load()
    for x in range(0, width):
        for y in range(0, height):
            if pix[x, y]==0:
                pix[x, y]=255
            else:
                pix[x, y]=0
    im.save('piece'+str(piece)+'.png')

def swap(piece1, piece2):
    im = Image.open('piece'+str(piece1)+'.png')
    pix = im.load()
    width, height = im.size
    for x in range(0, width):
        for y in range(0, height):
            if pix[x, y] == 255:
                pix[x, y] = 0
            else:
                pix[x, y] = 255
    im.save('piece'+str(piece1)+'.png')
    img = cv2.imread('piece'+str(piece1)+'.png', 0)
    rows, cols = img.shape
    M = np.float32([[1, 0, pieces[piece2][0]-pieces[piece1][0]], [0, 1, pieces[piece2][1]-pieces[piece1][1]]])
    dst = cv2.warpAffine(img, M, (cols, rows))
    img = Image.fromarray(dst)
    img.save('piece'+str(piece1)+'.png')
    im = Image.open('piece'+str(piece1)+'.png')
    pix = im.load()
    for x in range(0, width):
        for y in range(0, height):
            if pix[x, y] == 0:
                pix[x, y] = 255
            else:
                pix[x, y] = 0
    im.save('piece'+str(piece1)+'.png')

    im = Image.open('piece' + str(piece2) + '.png')
    pix = im.load()
    width, height = im.size
    for x in range(0, width):
        for y in range(0, height):
            if pix[x, y] == 255:
                pix[x, y] = 0
            else:
                pix[x, y] = 255
    im.save('piece' + str(piece2) + '.png')
    img = cv2.imread('piece' + str(piece2) + '.png', 0)
    rows, cols = img.shape
    M = np.float32([[1, 0, pieces[piece1][0]-pieces[piece2][0]], [0, 1, pieces[piece1][1]-pieces[piece2][1]]])
    dst = cv2.warpAffine(img, M, (cols, rows))
    img = Image.fromarray(dst)
    img.save('piece' + str(piece2) + '.png')
    im = Image.open('piece' + str(piece2) + '.png')
    pix = im.load()
    for x in range(0, width):
        for y in range(0, height):
            if pix[x, y] == 0:
                pix[x, y] = 255
            else:
                pix[x, y] = 0
    im.save('piece' + str(piece2) + '.png')
    temp = pieces[piece1]
    pieces[piece1]= pieces[piece2]
    pieces[piece2] = temp

def connect(piece1, piece2):
    im = Image.open('piece' + str(piece1) + '.png')
    pix = im.load()
    width, height = im.size
    for x in range(0, width):
        for y in range(0, height):
            if pix[x, y] == 255:
                pix[x, y] = 0
            else:
                pix[x, y] = 255
    im.save('piece' + str(piece1) + '.png')
    img = cv2.imread('piece' + str(piece1) + '.png', 0)
    rows, cols = img.shape
    M = np.float32([[1, 0, (pieces[piece2][0] - pieces[piece1][0])/3], [0, 1, (pieces[piece2][1] - pieces[piece1][1])/3]])
    dst = cv2.warpAffine(img, M, (cols, rows))
    img = Image.fromarray(dst)
    img.save('piece' + str(piece1) + '.png')
    im = Image.open('piece' + str(piece1) + '.png')
    pix = im.load()
    for x in range(0, width):
        for y in range(0, height):
            if pix[x, y] == 0:
                pix[x, y] = 255
            else:
                pix[x, y] = 0
    im.save('piece' + str(piece1) + '.png')

if __name__=="__main__":
    im = Image.open('frozenblack.jpg') # Can be many different formats.
    pix = im.load()
    print("Puzzle Dimensions: "+str(im.size))  # Get the width and hight of the image for iterating over
    width, height = im.size
    for x in range(0, width):
        for y in range(0, height):
            if pix[x, y][0]<130 and pix[x, y][1]<130 and pix[x, y][2]<130:
                pix[x, y]=(0, 0, 0)
    for x in range(0, width):
        for y in range(0, height):
            if pix[x, y]!=(0, 0, 0):
                pix[x, y]=(0, 0, 0)
            else:
                pix[x, y]=(255, 255, 255)
    for x in range(width-70, width):
        for y in range(0, height):
            pix[x, y]=(255, 255, 255)
    im.save('frozen.png')  # Save the modified pixels as .png

    for k in range(1, 5):
        im = Image.open('frozen.png')
        pix = im.load()
        if k!=1:
            for x in range(0, int(width/2)):
                for y in range(0, int(height/2)):
                    pix[x, y]=(255, 255, 255)
        if k!=2:
            for x in range(int(width/2), width):
                for y in range(0, int(height/2)):
                    pix[x, y]=(255, 255, 255)
        if k!=3:
            for x in range(0, int(width/2)):
                for y in range(int(height/2), height):
                    pix[x, y]=(255, 255, 255)
        if k!=4:
            for x in range(int(width/2), width):
                for y in range(int(height/2), height):
                    pix[x, y]=(255, 255, 255)
        im.save('piece'+str(k)+'.png')

    for num in range(1, 5):
        piece = Image.open('piece' + str(num) + '.png')
        piece = piece.load()
        m = np.zeros((width, height))
        for x in range(width):
            for y in range(height):
                m[x, y] = piece[(x, y)] != (255, 255, 255)
        m = m / np.sum(np.sum(m))
        dx = np.sum(m, 1)
        dy = np.sum(m, 0)
        cx = int(np.sum(dx * np.arange(width)))
        cy = int(np.sum(dy * np.arange(height)))
        pieces[num]=[cx, cy]

        img = cv2.imread('piece'+str(num)+'.png')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges2 = cv2.Canny(gray, 50, 150, apertureSize=3)

        lines = cv2.HoughLines(edges2, 1, np.pi / 180, 165)

        if lines is not None:
            if len(lines) == 1:
                edges[num] = [cx, cy]
            if len(lines) == 2:
                corners[num] = [cx, cy]
        else:
            interior[num]= [cx, cy]
        img = cv2.imread('piece'+str(num)+'.png', 0)
        img = Image.fromarray(img)
        img.save('piece'+str(num)+'.png')

    print("All Pieces: " + str(pieces))
    print("Corner Pieces: " + str(corners))
    print("Edge Pieces: " + str(edges))
    print("Interior Pieces: " + str(interior))
    print("Solve Directions: Rotate Piece 3 272 degrees counterclockwise, swap locations of Piece 1 and Piece 4, and assemble pieces.")
    rotate(3, pieces[3], 272)
    swap(1, 4)
    connect(1, 3)
    connect(2, 3)
    connect(4, 3)
    im = Image.open('frozenblack.jpg')
    pix = im.load()
    im1 = Image.open('piece1.png')
    pix1 = im1.load()
    im2 = Image.open('piece2.png')
    pix2 = im2.load()
    im3 = Image.open('piece3.png')
    pix3 = im3.load()
    im4 = Image.open('piece4.png')
    pix4 = im4.load()
    for x in range(0, width):
        for y in range(0, height):
            if pix1[x,y]==0 or pix2[x, y]==0 or pix3[x, y]==0 or pix4[x,y]==0:
                pix[x,y]=(0,0,0)
            else:
                pix[x,y]=(255, 255, 255)
    im.save("frozensolved.png")
    print("Puzzle solved.")