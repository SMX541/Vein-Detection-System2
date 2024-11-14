import cv2
import numpy as np
import os

def process_image(image_path, output_path):
    # Check if the image file exists
    if not os.path.exists(image_path):
        print(f"Error: The image at {image_path} does not exist.")
        return

    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Failed to load the image at {image_path}. Please check the file format and permissions.")
        return

    # Convert to grayscale
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except cv2.error as e:
        print(f"Error: {str(e)}")
        return

    # Apply CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    try:
        cl1 = clahe.apply(gray)
    except cv2.error as e:
        print(f"Error during CLAHE application: {str(e)}")
        return

    # Save the processed image
    cv2.imwrite(output_path, cl1)
    print(f"Processed image saved at {output_path}")

def main():
    # Define paths for the input and output images
    input_image_path = 'current_frame.jpg'  # This should be the same image captured from the camera
    output_image_path = 'processed_image.jpg'

    # Process the image
    process_image(input_image_path, output_image_path)

if __name__ == "__main__":
    main()
