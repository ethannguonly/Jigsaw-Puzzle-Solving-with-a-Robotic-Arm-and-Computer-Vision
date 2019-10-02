#tamp down
import pyuarm
width = 2016
height = 1504
arm.connect()
for x in range(0, 4):
    for y in range(0, 3):
        arm.set_position(x=width/4*(0.5+x), y = height/3*(0.5+y), z = 50)
        arm.set_position(x=width/4*(0.5+x), y = height/3*(0.5+y), z = 0)
        arm.set_position(x=width/4*(0.5+x), y = height/3*(0.5+y), z = 50)


#find the exact pixel coordinate for the bottom left corner and send the first corner there with the edges facing outside the board