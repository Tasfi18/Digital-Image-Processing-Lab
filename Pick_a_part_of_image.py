import cv2
import numpy as np

# Load the original image
image = cv2.imread("C:/Users/USER/Videos/Captures/TBD/dip lab/pngtree-blue-bird-vector-or-color-illustration-png-image_2013004.jpg")

# Define the coordinates for the crop (x, y, width, height)
# You can adjust these values to fit the area you want to crop
x, y, w, h = 100, 100, 200, 200

# Crop the image using array slicing
cropped_image = image[y:y+h, x:x+w]

# Create a black rectangle over the cropped area in the original image
image_with_blackout = image.copy()
image_with_blackout[y:y+h, x:x+w] = [0, 0, 0]  # Blackout the cropped region

# Display the original image with blackout and the cropped part
cv2.imshow('Original Image with Blackout', image_with_blackout)
cv2.waitKey(100)

cv2.imshow('Cropped Part', cropped_image)
cv2.waitKey(0)
#cv2.destroyAllWindows()

# Optionally, save the images
cv2.imwrite('image_with_blackout.jpg', image_with_blackout)
cv2.imwrite('cropped_part.jpg', cropped_image)
