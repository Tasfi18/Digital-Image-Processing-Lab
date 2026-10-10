# Digital Image Processing Lab

Image processing exercises from the Digital Image Processing lab course, written in Python with OpenCV, NumPy, Pillow and Matplotlib. Most of the operations are written out pixel by pixel instead of calling a library function, to show how they work.

![Original, log transform (c = 30), scaled log transform and power-law transform (γ = 2)](docs/intensity_transforms.png)

*Left to right: the original, log transform with c = 30, log transform scaled to the full range, power-law transform with γ = 2.*

## Exercises

| Script | What it does | Input | Output |
| --- | --- | --- | --- |
| `read_image.py` | Reads an image and prints it as a NumPy array | `man-8554081_640.webp` | (window) |
| `grayscale_conversion.py` | Converts a colour image to grayscale | `demo5.jpg` | (window) |
| `negative_conversion.py` | Image negative, `s = 255 − r` | `demo5.jpg` | `negative_image.jpg` |
| `crop_region.py` | Cuts out a 200×200 region and blacks it out in the original | `demo5.jpg` | `cropped_part.jpg`, `image_with_blackout.jpg` |
| `gray_to_color.py` | Pseudo-colour: dark tones blue, mid-tones green, bright tones red | `man-8554081_640.webp` | `colorized_image.jpg` |
| `log_transform.py` | Log transform, `s = c · log(1 + r)`, with a fixed and a full-range `c` | `demo5.jpg` | `LogTransform.jpeg`, `ScaledLogTransform.jpeg` |
| `power_law_transform.py` | Power-law (gamma) transform, `s = c · r^γ` on 0–1 values | `demo5.jpg` | `PowerLawTransform.jpeg` |
| `histogram_equalization.py` | Histogram equalization from the PDF and CDF, with before and after histograms | `demo4.jpg` | `equalized_image.png` |
| `histogram_equalization2.py` | The same, also showing the images | `demo4.jpg` | `equalized_image.png` |
| `histogram_matching.py` | Matches the histogram to a Gaussian (or exponential) distribution | `demo4.jpg` | `histogram_matched.png` |
| `histogram_matching2.py` | The same, also plotting the input, target and result histograms | `demo4.jpg` | `histogram_matched.png` |

Scripts read their input from, and save their output to, the folder they are in, so they run from anywhere.

## Run

Python 3.10 or later.

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python histogram_equalization2.py
```

OpenCV windows close when you press a key.

## Tests

```bash
pip install -r requirements-dev.txt
python -m pytest
```

8 tests cover the log and power-law transforms, histogram counting, CDF normalisation and the histogram-matching lookup table. GitHub Actions runs them on every push.
