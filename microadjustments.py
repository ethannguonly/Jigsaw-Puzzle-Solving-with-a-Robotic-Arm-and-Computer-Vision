detect if there is green in puzzle still means that not in
find center of mass of the piece and find center of mass of the blank where the piece should go and move the piece there


Tamp down pieces:

height to 1 on the centers of mass of every piece in the puzzle


#see if there is a green pixel between the pieces
stillgreeen = []
for x in range(0, width):
    for y in range(0, height):
        if pix[x, y][0] >= 42 and pix[x, y][0] <= 72:
            if pix[x, y][1] >= 236:
                if pix[x, y][2] >= 10 and pix[x, y][2] <= 30:
                    stillgreeen.append([x, y])

#center of mass
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
pieces[num] = [cx, cy]


puzzle = Image.open('puzzleref.png')





