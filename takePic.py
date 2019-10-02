import os
import time
import glob
from PIL import Image

os.system('cd platform-tools && adb shell "input keyevent 27"')
time.sleep(1)
# \Galaxy J3\Phone\DCIM\Camera
os.system('cd platform-tools && adb pull /sdcard/DCIM/Camera')
filename = max(glob.glob("platform-tools/Camera/*.*"), key=os.path.getmtime)
img = Image.open(filename)
img = img.resize((2016, 1504))
img.save("./images/samples/green.jpg", "JPEG", optimize=True)

# import urllib.request
# import cv2# import numpy as np

# # Replace the URL with your own IPwebcam shot.jpg IP:port
# url='http://[2607:fc20:1393:ddf4:0:36:eb56:5801]:8080/shot.jpg'

# while True:

# # Use urllib to get the image from the IP camera
#  imgResponse = urllib.request.urlopen(url)
 
#  # Numpy to convert into a array
#  imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
 
#  # Decode the array to OpenCV usable format
#  img = cv2.imdecode(imgNp,-1)
 
 
#  # put the image on screen
#  cv2.imshow('IPWebcam',img)

# # Program closes if q is pressed
#  if cv2.waitKey(1) & 0xFF == ord('q'):
#  	break