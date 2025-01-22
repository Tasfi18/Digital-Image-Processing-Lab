import cv2 
import numpy as np

# Read the image
image_path = "C:/Users/USER/Videos/Captures/TBD/dip lab/man-8554081_640.webp"
image = cv2.imread(image_path)

# Convert to an array
image_array = np.array(image)

# Display the image
cv2.imshow("C:/Users/USER/Videos/Captures/TBD/dip lab/man-8554081_640.webp", image)
cv2.waitKey(0)

# Display the array
print('Image Array Shape:', image_array.shape)
print('Image Array:\n', image_array)
