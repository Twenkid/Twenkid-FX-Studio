import pygame
import pygame.camera
import time
'''
 Reading camera with PyGame 2.0 and converting the image to OpenCV.
 Requires also VideoCapture packet.
 A workaround to read from camera in OpenCV if there's error with Media Foundation Drivers for the webcam
 which cause cap = cv2.VideoCapture(0) -->  cap.read() to fail 
Z:\py>python cli.py
[ WARN:0] global C:\Users\appveyor\AppData\Local\Temp\1\pip-req-build-i1s8y2i1\o
pencv\modules\videoio\src\cap_msmf.cpp (677) CvCapture_MSMF::initStream Failed t
o set mediaType (stream 0, (640x480 @ 30) MFVideoFormat_RGB24(codec not found)
Traceback (most recent call last):
  File "cli.py", line 62, in <module>
    main()
  File "cli.py", line 55, in main
    video_stream()
  File "cli.py", line 46, in video_stream
    ret, frame = cap.read()
KeyboardInterrupt
'''

#C:\Windows\system32>python -m pip install VideoCapture
#Collecting VideoCapture
#Downloading VideoCapture-0.9.5-cp38-cp38-win_amd64.whl (90 kB)
#   90 kB 1.4 MB/s
#Installing collected packages: VideoCapture
#Successfully installed VideoCapture-0.9.5
#WARNING: You are using pip version 20.2.3; however, version 20.3.3 is available.
#pygame 2.0.

#You should consider upgrading via the 'C:\Program Files\Python38\python.exe -m p
#ip install --upgrade pip' command.

# 11-1-2021
# If OpenCV camera doesn't work - Windows Media Foundations issues Win 7 ...


pygame.camera.init()
cameras = pygame.camera.list_cameras()
#pygame.camera.list_cameras()
print(cameras)
#cam = pygame.camera.Camera("/dev/video0", (640, 480))
#cam = pygame.camera.Camera(cameras[0], (640, 480))
cam = pygame.camera.Camera(0, (640, 480))
cam.start()
time.sleep(0.1)  # You might need something higher in the beginning
img = cam.get_image()
pygame.image.save(img, "pygame.jpg")
print(img.get_size())
w,h = img.get_size()
print(dir(img))
#image = img.get_view()
import cv2
import numpy as np
#output = np.zeros((h, w, 3), np.uint8)
output = np.zeros((h*w*3), np.uint8)
#output = ((h,w, 3), np.uint8)
cv2.imshow("GUZ1", output)
image_string = pygame.image.tostring(img, 'RGB') #surface_to_string(img)
#print(image_string)
print(len(image_string))
#output[:] = image_string
#for n,i in enumerate(image_string):
#  output[n] = i  
'''
for n,i in enumerate(image_string):
  output[n] = i
'''

for i in range(h*w*3):
  output[i] = image_string[i]
  
#print(type(image_string)) #Bytes
'''  
output[:] = np.array(image_string, np.uint8)#.reshape(h*w*3)
Traceback (most recent call last):
  File "cam.py", line 57, in <module>
    output[:] = np.array(image_string[1:], np.uint8)#.reshape(h*w*3)
ValueError: invalid literal for int() with base 10: b'\x05\x1a2\x03\x17.\t\x0c/\
n\r%\x11\x11"\r\r\x1e\x0e\x11\x1e\x0e\x11\x1f\x0c\x0e\x1e\x0b\r\x1d\x0b\x08\x1e\
x0c\t\x1f\x0c\x07\x1e\n\x06"\t\r\'\r\x12.\x0b\x1e.\x0b\x1e)\t\x1a)\t\x1a&\t\x13$
\x07\x11\x1e
'''

##output[:] = image_string doesn't work etc.
#output[:] = bytes(image_string) doesn't work etc.
#output[:] = image_string  #no

#output = np.zeros((h, w, 3), np.uint8)
#import numpy as np
#output.reshape((h, w, 3))
output = output.reshape((480, 640, 3))
output = cv2.cvtColor(output, cv2.COLOR_RGB2BGR) 
print(w,h,3)

#c = cv2.cvtColor(output, cv2.COLOR_RGB2BGR) 

#cv2.imshow("GUZ", c)
cv2.imshow("GUZ", output)
cv2.waitKey()
cam.stop()
