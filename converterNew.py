import sys, math

transX, transY, transAng = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])

coordFile = open('coords.txt', 'r+')
angleFile = open('angles.txt', 'r+')
output = open('output.txt', 'w+')
oldSet = set()
newSet = set()
deltaX, deltaY = 0, 0
line = ''
initial = set()
endState = []
endStateTrans = []
angles = []
for x in range(0, int(sys.argv[4])):
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
		# print(initial)
		newSet = set()
	else:
		notSim = oldSet ^ newSet
		oldSet = newSet
		newSet = set()
		li = [t for t in notSim]

		if li[0] in oldSet:
			ang = float(angleFile.readline().replace('\n', ''))
			# if x == 1:
			# 	deltaX = transX - li[0][0]
			# 	deltaY = transY - li[0][1]

			# #var rotatedX = Math.cos(angle) * (point.x - center.x) - Math.sin(angle) * (point.y-center.y) + center.x;
			# #var rotatedY = Math.sin(angle) * (point.x - center.x) + Math.cos(angle) * (point.y - center.y) + center.y;

			# # outputX = li[0][0] + deltaX
			# # outputY = li[0][1] + deltaY
			# # ang = ang + transAng

			# ang = ang + transAng
			# transAng = transAng * (math.pi/180)
			# outputX = math.cos(transAng) * (li[0][0] + deltaX - transX) - math.sin(transAng)*(li[0][1] + deltaY - transY) + transX
			# outputY = math.sin(transAng) * (li[0][0] + deltaX - transX) + math.cos(transAng)*(li[0][1] + deltaY - transY) + transY
			

			if ang > 180:
				ang = ang - 360
			endState.append(li[1])
			endStateTrans.append(li[0])
			angles.append(ang)
			# print(str(li[1]) + ",",str(li[0]) + ",", 'Angle:', ang, file = output)
		else:
			ang = float(angleFile.readline().replace('\n', ''))
			# if x == 1:
			# 	deltaX = transX - li[1][0]
			# 	deltaY = transY - li[1][1]

			# # outputX = li[1][0] + deltaX
			# # outputY = li[1][1] + deltaY
			# # ang = ang + transAng

			# ang = ang + transAng
			# transAng = transAng * (math.pi/180)`
			# outputX = math.cos(transAng) * (li[1][0] + deltaX - transX) - math.sin(transAng)*(li[1][1] + deltaY - transY) + transX
			# outputY = math.sin(transAng) * (li[1][0] + deltaX - transX) + math.cos(transAng)*(li[1][1] + deltaY - transY) + transY

			if ang > 180:
				ang = ang - 360
			endState.append(li[0])
			endStateTrans.append(li[1])
			angles.append(ang)
			# print(str(li[0]) + ",",str(li[1]) + ",", 'Angle:', ang, file = output)


first = (initial ^ set(endState)).pop()

if(transX == -1):
	# print(str(first) + ",",str(first) + ",", 'Angle:', 0, file = output)
	print(first[0], first[1], first[0], first[1], 0, file = output)
	for x in range(0, len(endState)):
		# print(str(endState[x]) + ",",str(endStateTrans[x]) + ",", 'Angle:', angles[x], file = output)
		print(endState[x][0], endState[x][1], endStateTrans[x][0], endStateTrans[x][1], angles[x], file = output)

else:
	# print(str(transX) + ",",str(transY) + ",", 'Angle:', transAng, file = output)
	print(first[0], first[1], transX, transY, transAng, file = output)
	deltaX = transX - first[0]
	deltaY = transY - first[1]
	for x in range(0, len(endState)):
		tAng = transAng * (math.pi/180)
		outputX = math.cos(tAng) * ((endStateTrans[x][0] + deltaX) - transX) - math.sin(tAng)*((endStateTrans[x][1] + deltaY) - transY) + transX
		outputY = math.sin(tAng) * ((endStateTrans[x][0] + deltaX) - transX) + math.cos(tAng)*((endStateTrans[x][1] + deltaY) - transY) + transY		
		# print(str(outputX) + ",",str(outputY) + ",", 'Angle:', angles[x] + transAng, file = output)
		print(endState[x][0], endState[x][1], outputX, outputY, angles[x] + transAng, file = output)