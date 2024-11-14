# import the necessary packages
import cv2
import numpy as np
import subprocess
import time

def nothing(x):
    pass

# Create a window
cv2.namedWindow('image')

# Create trackbars for color change
cv2.createTrackbar('CLimit', 'image', 0, 8, nothing)
r = 1.4

def capture_image():
    # Capture an image using libcamera-still
    subprocess.run(['libcamera-still', '-o', 'current_frame.jpg'])

# Capture initial image
capture_image()

# Allow the camera to warmup
time.sleep(0.1)

while True:
    # Read the image captured by libcamera
    image = cv2.imread('current_frame.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Our operations on the frame come here
    # Convert and put CLAHE
    clahe = cv2.createCLAHE(clipLimit=r, tileGridSize=(9,9))
    cl1 = clahe.apply(gray)
   
    # Display the resulting frame
    cv2.imshow("image", cl1)
    k = cv2.waitKey(1) & 0xFF

    # Capture the image on screen by pressing 'a' and break
    if k == ord("a"):
        cv2.imwrite(time.strftime("Screenshot%Y%m%d%H%M%S.jpg"), cl1)
        cv2.imwrite("temp.jpg", cl1)
        break

    # If the `q` key was pressed, break from the loop
    if k == ord("q"):
        break
    
    # Get current positions of trackbar
    p = cv2.getTrackbarPos('CLimit', 'image')
    r = 0.5 + (p/2)
    
    # Capture a new image for the next frame
    capture_image()

# When everything done, destroy all the windows
cv2.destroyAllWindows()
