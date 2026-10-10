import cv2
from pathlib import Path

# Images are read from and saved next to this script.
HERE = Path(__file__).resolve().parent

# Read the image
image = cv2.imread(str(HERE / "demo5.jpg"))

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original image
cv2.imshow("Original Image", image)
cv2.waitKey(1000)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)

#cv2.destroyAllWindows()