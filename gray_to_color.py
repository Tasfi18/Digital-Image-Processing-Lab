import cv2
import numpy as np
from pathlib import Path

# Images are read from and saved next to this script.
HERE = Path(__file__).resolve().parent

# Read the grayscale image
gray_image = cv2.imread(str(HERE / "man-8554081_640.webp"), cv2.IMREAD_GRAYSCALE)

# Convert the grayscale image to a 3-channel (BGR) image
color_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

# Manually apply color mapping: 
# (blue for dark areas, green for mid-tone, red for bright areas)

# Create a color mask based on intensity ranges
color_image[gray_image <= 85] = [150, 0, 0]   # Blue for dark areas
color_image[(gray_image > 85) & (gray_image <= 170)] = [0, 150, 0]  # Green for mid-tone
color_image[gray_image > 170] = [0, 0, 150]   # Red for bright areas

# Display the original grayscale and artificially colorized images
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(1000)

cv2.imshow('Colorized Image', color_image)
cv2.waitKey(0)

cv2.destroyAllWindows()

# Optionally, save the colorized image
cv2.imwrite(str(HERE / "colorized_image.jpg"), color_image)
