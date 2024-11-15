import numpy as np
import cv2
from matplotlib import pyplot as plt

# Attempt to load the images
img = cv2.imread('/Users/shubhrajitdutta/CODE1/vcpkg/DSA-C++/vin2.jpeg', 0)

# Check if the image was loaded correctly
if img is None:
    raise FileNotFoundError("Image file 'temp.jpg' not found. Check the file path.")

# Define kernel for morphological transformations
kernel = np.ones((5,5), np.uint8)

# Create a CLAHE object (Arguments are optional)
clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(7,7))
cl1 = clahe.apply(img)

# Apply median blur to the image
cl2 = cv2.medianBlur(cl1, 5)

# Apply adaptive threshold
th1 = cv2.adaptiveThreshold(cl2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 2.55)

# Apply Otsu's threshold
blur = cv2.GaussianBlur(cl1, (5,5), 0)
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Removing noise using bitwise AND operation
th2 = th1 & th3

# Apply morphological opening
opening = cv2.morphologyEx(th2, cv2.MORPH_OPEN, kernel)

# Find contours
contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Convert the grayscale image to BGR for contour drawing
img1 = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
dst = cv2.drawContours(img1, contours, -1, (0, 255, 0), -1)

# Save the output images
cv2.imwrite("out.jpg", dst)
cv2.imwrite("dst.jpg", dst)

# Display the output (Optional)
plt.imshow(dst)
plt.title('Contours')
plt.show()
