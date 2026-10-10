import cv2
import numpy as np
from pathlib import Path

# Images are read from and saved next to this script.
HERE = Path(__file__).resolve().parent

# Read the image
image = cv2.imread(str(HERE / "demo5.jpg"))

# Create the negative image by subtracting the pixel values from 255
negative_image = 255 - image

# Display the original and negative images
cv2.imshow('Original Image', image)
cv2.waitKey(1000)

cv2.imshow('Negative Image', negative_image)
cv2.waitKey(0)

#cv2.destroyAllWindows()

# Save the negative image
cv2.imwrite(str(HERE / "negative_image.jpg"), negative_image)
