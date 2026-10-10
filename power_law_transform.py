from PIL import Image
import numpy as np
from pathlib import Path

# Images are read from and saved next to this script.
HERE = Path(__file__).resolve().parent


def power_law_transform(r, gamma, c=1.0):
    """Gamma correction: s = c * r^gamma, with r scaled to 0..1 first.

    gamma > 1 darkens the image, gamma < 1 brightens it.
    """
    normalized = r.astype(np.float64) / 255
    s = c * normalized ** gamma * 255
    return np.clip(np.round(s), 0, 255).astype(np.uint8)


if __name__ == "__main__":
    image = Image.open(str(HERE / "demo5.jpg"))
    r = np.array(image.convert('L'))

    s = power_law_transform(r, gamma=2)
    Image.fromarray(s).save(HERE / "PowerLawTransform.jpeg")
    Image.fromarray(s).show()
