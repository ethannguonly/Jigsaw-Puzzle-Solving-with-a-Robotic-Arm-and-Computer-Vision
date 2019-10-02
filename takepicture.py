import os
import time
import glob
from PIL import Image
os.system('platform-tools/./adb shell "input keyevent 27"')
time.sleep(1)
os.system('platform-tools/./adb pull /sdcard/DCIM/Camera')
filename = max(glob.glob("Camera/*.*"), key=os.path.getmtime)
img = Image.open(filename)
img = img.resize((2016, 1504))
img.save("puzzlestate.jpg", "JPEG", optimize=True)