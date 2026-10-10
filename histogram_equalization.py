import numpy as np
import cv2
import matplotlib.pyplot as plt
from pathlib import Path

# Images are read from and saved next to this script.
HERE = Path(__file__).resolve().parent


image = cv2.imread(str(HERE / "demo4.jpg"), cv2.IMREAD_GRAYSCALE)

height, width = image.shape
num_pixels = height * width

histogram = np.zeros(256)
for i in range(height):
    for j in range(width):
        pixel_value = image[i, j]
        histogram[pixel_value] += 1

pdf = histogram / num_pixels

cdf = np.zeros(256)
cdf[0] = pdf[0]
for i in range(1, 256):
    cdf[i] = cdf[i - 1] + pdf[i]

cdf_normalized = np.round(cdf * 255).astype(np.uint8)

equalized_image = np.zeros_like(image)
for i in range(height):
    for j in range(width):
        equalized_image[i, j] = cdf_normalized[image[i, j]]

cv2.imwrite(str(HERE / "equalized_image.png"), equalized_image)

original_histogram = histogram
equalized_histogram = np.zeros(256)
for i in range(height):
    for j in range(width):
        equalized_histogram[equalized_image[i, j]] += 1

print("Original Histogram:", original_histogram)
print("Equalized Histogram:", equalized_histogram)

plt.figure(figsize=(12, 6))

# Plot original histogram
plt.subplot(1, 2, 1)
plt.bar(range(256), histogram, color='blue', alpha=0.7)
plt.title('Original Histogram')
plt.xlim([0, 255])
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Plot equalized histogram
plt.subplot(1, 2, 2)
plt.bar(range(256), equalized_histogram, color='green', alpha=0.7)
plt.title('Equalized Histogram')
plt.xlim([0, 255])
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Show the histograms
plt.tight_layout()
plt.show()