# import the necessary packages
import cv2
import numpy as np
import subprocess
import time

def nothing(x):
    pass

# Initialize camera with libcamera
def capture_image():
    # Capture an image using libcamera-still
    subprocess.run(['libcamera-still', '-o', 'image.jpg'])

# Create a window
cv2.namedWindow('image')

# Load a predefined image
img1 = cv2.imread('out.jpg')
rows, cols, channels = img1.shape

# Capture an image to start
capture_image()

# allow the camera to warmup
time.sleep(0.1)

# Read the image captured by libcamera
image = cv2.imread('image.jpg')
roi = image[0:rows, 0:cols]

while True:
    # Display the resulting frame
    dst = cv2.addWeighted(image, 0.7, img1, 0.3, 0)
    cv2.imshow("image", dst)
    k = cv2.waitKey(1) & 0xFF

    if k == ord("a"):
        # Save the image with a timestamp
        cv2.imwrite(time.strftime("Vein_Screenshot%Y%m%d%H%M%S.jpg"), dst)
        break

    if k == ord("q"):
        # If 'q' is pressed, exit loop
        break

    # Capture a new image for the next frame
    capture_image()
    image = cv2.imread('image.jpg')
    roi = image[0:rows, 0:cols]

# When everything is done, destroy all the windows
cv2.destroyAllWindows()


