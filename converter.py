import sys, math


transX, transY, transAng = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
# 100, 1450

coordFile = open('coords.txt', 'r+')
angleFile = open('angles.txt', 'r+')
output = open('output.txt', 'w+')
oldSet = set()
newSet = set()
deltaX, deltaY = 0, 0
line = ''
initial = set()
for x in range(0, 3):
	line = coordFile.readline()
	while True:
		if line == '\n':
			break
		tup = tuple([float(x) for x in line.split(" ")])
		newSet.add(tup)
		# print(tup)
		line = coordFile.readline()
	# print('\n')
	if oldSet == set():
		oldSet = newSet
		initial = newSet
		newSet = set()
	else:
		notSim = oldSet ^ newSet
		oldSet = newSet
		newSet = set()
		li = [t for t in notSim]

		if li[0] in oldSet:
			ang = float(angleFile.readline().replace('\n', ''))
			if x == 1:
				deltaX = transX - li[0][0]
				deltaY = transY - li[0][1]

			#var rotatedX = Math.cos(angle) * (point.x - center.x) - Math.sin(angle) * (point.y-center.y) + center.x;
			#var rotatedY = Math.sin(angle) * (point.x - center.x) + Math.cos(angle) * (point.y - center.y) + center.y;

			# outputX = li[0][0] + deltaX
			# outputY = li[0][1] + deltaY
			# ang = ang + transAng


			

			ang = ang + transAng
			transAng = transAng * (math.pi/180)
			outputX = math.cos(transAng) * (li[0][0] + deltaX - transX) - math.sin(transAng)*(li[0][1] + deltaY - transY) + transX
			outputY = math.sin(transAng) * (li[0][0] + deltaX - transX) - math.cos(transAng)*(li[0][1] + deltaY - transY) + transY
			

			if ang > 180:
				ang = ang - 360
			print(str(li[1]) + ",",str((outputX, outputY)) + ",", 'Angle:', ang, file = output)
		else:
			ang = float(angleFile.readline().replace('\n', ''))
			if x == 1:
				deltaX = transX - li[1][0]
				deltaY = transY - li[1][1]

			# outputX = li[1][0] + deltaX
			# outputY = li[1][1] + deltaY
			# ang = ang + transAng

			ang = ang + transAng
			transAng = transAng * (math.pi/180)
			outputX = math.cos(transAng) * (li[1][0] + deltaX - transX) - math.sin(transAng)*(li[1][1] + deltaY - transY) + transX
			outputY = math.sin(transAng) * (li[1][0] + deltaX - transX) - math.cos(transAng)*(li[1][1] + deltaY - transY) + transY

			if ang > 180:
				ang = ang - 360
			print(str(li[0]) + ",",str((outputX, outputY)) + ",", 'Angle:', ang, file = output)