from PIL import Image
import cv2

numpieces = 4
puzzlewidth = 2
puzzleheight = 2

if __name__=="__main__":
    img = cv2.imread("frozenblack.jpg")
    height, width, channels = img.shape
    scaleheight = int(height / puzzleheight)
    scalewidth = int(width / puzzlewidth)
    for x in range(0, numpieces):
        y1 = x%puzzleheight*scaleheight
        y2 = (x%puzzleheight+1)*scaleheight
        x1 = x%puzzlewidth*scalewidth
        x2 = (x%puzzlewidth+1)*scalewidth
        crop_img = img[y1:y2, x1:x2]
        cv2.imwrite("piece"+str(x+1)+".png", crop_img)

        im = Image.open("piece"+str(x+1)+".png")
        im = im.convert("RGBA")
        datas = im.getdata()

        newData = []
        for item in datas:
            if item[0] < 132 and item[1] < 132 and item[2] < 132:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        im.putdata(newData)
        im.save("piece"+str(x+1)+".png", "PNG")