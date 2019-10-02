import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

img = cv2.imread('frozen.png')
gray= cv2.imread('frozen.png',0)

# Threshold to detect rectangles independent from background illumination
ret2,th3 = cv2.threshold(gray,220,255,cv2.THRESH_BINARY_INV)

# Detect contours
_, contours, hierarchy = cv2.findContours( th3.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Draw contours
h, w = th3.shape[:2]
vis = np.zeros((h, w, 3), np.uint8)
cv2.drawContours( vis, contours, -1, (128,255,255), -1)

# Print Features of each contour and select some contours
contours2=[]
for i, cnt in enumerate(contours):
    cnt=contours[i]
    M = cv2.moments(cnt)

    if M['m00'] != 0:
        # for definition of features cf http://docs.opencv.org/3.1.0/d1/d32/tutorial_py_contour_properties.html#gsc.tab=0
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        area = cv2.contourArea(cnt)
        x,y,w,h = cv2.boundingRect(cnt)
        aspect_ratio = float(w)/h
        rect_area = w*h
        extent = float(area)/rect_area

        print(i, cx, cy, area, aspect_ratio, rect_area, extent)

        if area < 80 and area > 10:
            contours2.append(cnt)

# Detect Harris corners
dst = cv2.cornerHarris(th3,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None, iterations=5)

# Threshold for an optimal value, it may vary depending on the image.
harris=img.copy()
print(harris.shape)
harris[dst>0.4*dst.max()]=[255,0,0]

titles = ['Original Image', 'Thresholding', 'Contours', "Harris corners"]
images = [img, th3, vis, harris]
im = Image.fromarray(vis)
im.save("frozen3.png")
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()