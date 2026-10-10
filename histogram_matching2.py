import numpy as np
import cv2
import matplotlib.pyplot as plt
from pathlib import Path

# Images are read from and saved next to this script.
HERE = Path(__file__).resolve().parent


def load_image(image_path):
    img = cv2.imread(image_path, 0)
    return img

def calculate_histogram(img):
    height, width = img.shape
    histogram = np.zeros(256)
    for i in range(height):
        for j in range(width):
            pixel_value = img[i, j]
            histogram[pixel_value] += 1

    return histogram

def calculate_cdf(hist):
    cdf = np.zeros(256)
    cdf[0] = hist[0]
    for i in range(1, len(hist)):
        cdf[i] = cdf[i - 1] + hist[i]

    cdf_min = cdf[0]
    cdf_max = cdf[-1]
    if cdf_max == cdf_min:  # a single-colour image: nothing to spread out
        return cdf, np.full(256, 255, dtype=np.uint8)
    cdf_normalized = np.round((cdf - cdf_min) / (cdf_max - cdf_min) * 255).astype(np.uint8)

    return cdf, cdf_normalized

def generate_gaussian_distribution(size, mean = 127, std = 40):
    gaussian_hist = [0] * 256
    for i in range(size):
        value = int(mean + std * np.random.randn())
        if 0 <= value <= 255:
            gaussian_hist[value] += 1

    return gaussian_hist

def generate_exponential_distribution(size, scale=50):
    exponential_hist = [0] * 256
    for i in range(size):
        value = int(np.random.exponential(scale))
        if 0 <= value <= 255:
            exponential_hist[value] += 1
    return exponential_hist

def create_lookup_table(cdf_source, cdf_target):
    lookup_table = [0] * 256
    for i in range(256):
        diff = float('inf')
        closest_j = 0
        for j in range(256):
            # int() so the uint8 values don't wrap around when subtracted
            distance = abs(int(cdf_source[i]) - int(cdf_target[j]))
            if distance < diff:
                diff = distance
                closest_j = j
        lookup_table[i] = closest_j
    return lookup_table

def apply_lookup_table(img, lookup_table):
    img_flat = img.flatten()
    new_img_flat = [lookup_table[pixel] for pixel in img_flat]
    new_img = np.reshape(new_img_flat, img.shape).astype(np.uint8)
    return new_img

def plot_histograms(hist_input, hist_target, hist_matched, img, img_matched, distribution_type):
    plt.figure(figsize=(10, 8))

    plt.subplot(3, 2, 1)
    plt.bar(range(256), hist_input)
    plt.title('Input Image Histogram')

    plt.subplot(3, 2, 2)
    plt.bar(range(256), hist_target)
    plt.title(f'{distribution_type.capitalize()} Distribution Histogram')

    plt.subplot(3, 2, 3)
    plt.imshow(img, cmap='gray')
    plt.title('Input Image')

    plt.subplot(3, 2, 4)
    plt.imshow(img_matched, cmap='gray')
    plt.title(f'Histogram Matched Image ({distribution_type})')

    plt.subplot(3, 2, 5)
    plt.bar(range(256), hist_matched)
    plt.title('Matched Image Histogram')

    plt.tight_layout()
    plt.show()

def histogram_matching_manual(input_image_path, output_image_path, distribution_type='gaussian'):
    # Load the input image
    img = load_image(input_image_path)

    hist_input = calculate_histogram(img)
    cdf_input, cdf_input_normalized = calculate_cdf(hist_input)

    # Generate target histogram and CDF based on the distribution type
    if distribution_type == 'gaussian':
        hist_target = generate_gaussian_distribution(img.size)
    elif distribution_type == 'exponential':
        hist_target = generate_exponential_distribution(img.size)
    else:
        raise ValueError("distribution_type must be 'gaussian' or 'exponential'")

    cdf_target, cdf_target_normalized = calculate_cdf(hist_target)

    # Create the lookup table to map input histogram to target histogram
    lookup_table = create_lookup_table(cdf_input_normalized, cdf_target_normalized)

    # Apply the lookup table to get the matched image
    img_matched = apply_lookup_table(img, lookup_table)
    cv2.imwrite(output_image_path, img_matched)

    # Calculate histogram of the matched image
    hist_matched = calculate_histogram(img_matched)

    # Plot histograms and images
    plot_histograms(hist_input, hist_target, hist_matched, img, img_matched, distribution_type)

if __name__ == "__main__":
    input_image_path = str(HERE / "demo4.jpg")
    output_image_path = str(HERE / "histogram_matched.png")
    distribution_type = 'gaussian'

    histogram_matching_manual(input_image_path, output_image_path, distribution_type)

