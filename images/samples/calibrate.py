import numpy as np 
import cv2
import glob

criteria = (cv2.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeroes((6*7, 3) np.float32)
objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1,2)

objpoints = []
imgpoints = []

images = glob.glob("*jpg")

for fname in images:
	img = cv2.imread(fname)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)

	if ret == True:
		objpoints.append(objp)
		corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
		imgpoints.append(corners)

		cv2.drawChessboardCorners(img, (7, 6), corners2, ret)
		cv2.imshow('img', img)
		cv2.waitKey(500)
cv2.destroyAllWindows()