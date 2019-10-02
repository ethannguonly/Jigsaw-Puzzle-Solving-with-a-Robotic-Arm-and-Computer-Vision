import math
if __name__=="__main__":
    input("Pixel Coordinates: ")
    xcoordinate = (xpixel - width/ 2)
    ycoordinate = (length - ypixel)
    angle = math.atan(ycoordinate/xcoordinate)
    radius = math.sqrt(xcoordinate^2+ycoordinate^2)