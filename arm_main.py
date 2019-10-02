import pyuarm
import time
import numpy as np

offset = 10.2

def toXY(xpixel, ypixel, xtotal, ytotal):
	x = float(xpixel)/xtotal*91.44
	y = float(ypixel)/ytotal*60.96
	return(x,y)

def toPolar(x,y):
	rad = np.sqrt((x-45.72)**2 + (y-offset)**2)
	ang = np.arctan2(y-offset, x-45.72)*57.2958
	return(rad, ang)

def toServos(rad,ang):
	s1 = ang
	s2 = -0.00855*(rad**3)+0.484*(rad**2)-9.832*rad+128.410
	s3 = -0.00738*(rad**3)+0.488*(rad**2)-13.232*rad+211.377
	return(s1,s2,s3)

def armCoords(xTotal, yTotal, xpixel, ypixel, rotation):
	x,y = toXY(xpixel, ypixel, xTotal, yTotal)
	rad, ang = toPolar(x,y)
	s1,s2,s3 = toServos(rad, ang)
	s4 = rotation
	return(s1,s2,s3,s4)

def movArm(arm, angle0, angle1, angle2, angle3):
	arm.set_servo_angle(0, float(angle0))
	arm.set_servo_angle(1, float(angle1))
	arm.set_servo_angle(2, float(angle2))
	arm.set_servo_angle(3, float(angle3))

def main():

	arm = pyuarm.get_uarm()

	while True:
		loc = input("Pickup: XTotal YTotal XPixel YPixel Rotation: ")
		c = loc.split(" ")
		s1,s2,s3,s4 = armCoords(int(c[0]),int(c[1]),int(c[2]),int(c[3]),int(c[4]))

		loc = input("Drop: XTotal YTotal XPixel YPixel Rotation: ")
		d = loc.split(" ")
		s5,s6,s7,s8 = armCoords(int(d[0]),int(d[1]),int(d[2]),int(d[3]),int(d[4]))

		if(s1>=s5):
			r = 135
		if(s1<s5):
			r = 45

		movArm(arm, s1, s2+10, s3-10,r)
		arm.set_pump(True)
		time.sleep(0.5)
		movArm(arm, s1, s2+4, s3-4, r)
		time.sleep(0.5)
		movArm(arm, s1, s2, s3, r)
		time.sleep(0.5)
		movArm(arm, s1, s2+4, s3-4, r)
		time.sleep(0.65)
		movArm(arm, s1, s2+6, s3-6, r)
		time.sleep(0.65)
		movArm(arm, s1, s2+10, s3-10, r)
		time.sleep(0.5)
		movArm(arm, (s1+s5)/2, (s2+s6)/2+10, (s3+s7)/2-10, r+(s5-s1))
		time.sleep(0.5)
		movArm(arm, s5, s6+10, s7-10,r+(s5-s1))
		time.sleep(0.5)
		movArm(arm, s5, s6+4, s7-4, r+(s5-s1))
		time.sleep(0.5)
		movArm(arm, s5, s6, s7, r+(s5-s1))
		arm.set_pump(False)
		time.sleep(0.8)
		movArm(arm, s5, s6+4, s7-4, r+(s5-s1))
		time.sleep(0.5)
		movArm(arm, s5, s6+10, s7-10, r+(s5-s1))
		time.sleep(0.5)


main()