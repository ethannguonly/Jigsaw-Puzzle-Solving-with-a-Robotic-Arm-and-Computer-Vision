import pyuarm
import time
import numpy as np
from uarm.wrapper import SwiftAPI


res=(2016,1504)

p1 = (73, 1395)		#y = 315
p2 = (1959, 1333)   #y = -350
p3 = (945, 1127)	#x = 130
p4 = (930,498)		#x = 350
swift = SwiftAPI()
swift.reset()

coords = open("output.txt","r")
lines = coords.readlines()

for coord in lines:
	swift.reset()
	data = coord.split()

	x = data[1]
	y = data[0]

	x_out = -0.3498*int(float(x))/1932*2016+524.2 #+0.01*int(y)
	y_out = -0.355*int(float(y))/1449*1504+341 - 0.01*(1400-int(float(x)))

	swift.set_position(x = x_out, y = y_out, z = 15)
	swift.set_wrist(90)
	time.sleep(0.2)
	#down = input("Down? ")
	swift.set_pump(True)
	swift.set_position(x = x_out, y = y_out, z = 0)
	#up = input("Up? ")
	time.sleep(0.2)
	swift.set_position(x = x_out, y = y_out, z = 30)
	ang1 = swift.get_servo_angle()[0]


	x = data[3]
	y = data[2]
	r = data[4]

	x_out = -0.3498*int(float(x))+524.2 #+0.01*int(y)
	y_out = -0.355*int(float(y))+341 - 0.01*(1400-int(float(x)))

	swift.set_position(x = x_out, y = y_out, z = 15)
	time.sleep(6)
	ang2 = swift.get_servo_angle()[0]

	swift.set_wrist(90+(ang2-ang1))
	#down = input("Down? ")
	time.sleep(0.5)
	temp = 90+(ang2-ang1)
	swift.set_wrist(temp-int(float(r)))
	swift.set_position(x = x_out, y = y_out, z = 0)
	swift.set_pump(False)
	#up = input("Up? ")
	time.sleep(0.2)
	swift.set_position(x = x_out, y = y_out, z = 15)




