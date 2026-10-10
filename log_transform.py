from PIL import Image
import numpy as np
from pathlib import Path

# Images are read from and saved next to this script.
HERE = Path(__file__).resolve().parent


def log_transform(r, c):
    """s = c * log(1 + r), clipped to 0..255.

    The pixels are converted to float first: with uint8 values, 1 + 255 wraps
    around to 0 and the brightest pixels would turn black.
    """
    s = c * np.log1p(r.astype(np.float64))
    return np.clip(s, 0, 255).astype(np.uint8)


if __name__ == "__main__":
    image = Image.open(str(HERE / "demo5.jpg"))
    r = np.array(image.convert('L'))

    # A fixed constant brightens the dark areas but never reaches full white.
    s = log_transform(r, c=30)
    Image.fromarray(s).save(HERE / "LogTransform.jpeg")

    # Scaled so the brightest input (255) maps to 255.
    scaled = log_transform(r, c=255 / np.log(1 + 255))
    Image.fromarray(scaled).save(HERE / "ScaledLogTransform.jpeg")

    Image.fromarray(scaled).show()
