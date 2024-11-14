#!/bin/bash

# Automation script to handle image processing and file management
echo "Starting the vein detection process..."

# Create a new folder with a timestamp
Foldername=$(date "+%Y.%m.%d-%H.%M.%S")
mkdir -p "VeinDetectionData/$Foldername"

# Run the camera capture and processing scripts
echo "Capturing images..."
python RaspberryPi_cam.py
echo "Processing images..."
python Processing.py
echo "Generating output feed..."
python OutputFEED.py

# Remove temporary images
echo "Cleaning up temporary files..."
rm -f temp.jpg out.jpg

# Move all jpg images to the new directory
echo "Organizing images into directory: $Foldername"
mv *.jpg "VeinDetectionData/$Foldername/"

echo "Process completed successfully. All data moved to VeinDetectionData/$Foldername."
