import cv2
import numpy as np

def process_image(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load the image at {image_path}. Check the file path and permissions.")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(gray)

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
