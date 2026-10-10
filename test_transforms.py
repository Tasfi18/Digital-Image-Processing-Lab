import numpy as np

from histogram_matching import (
    apply_lookup_table,
    calculate_cdf,
    calculate_histogram,
    create_lookup_table,
)
from log_transform import log_transform
from power_law_transform import power_law_transform


def test_log_transform_keeps_white_pixels_bright():
    r = np.array([[0, 255]], dtype=np.uint8)
    s = log_transform(r, c=255 / np.log(256))
    assert s[0, 0] == 0
    assert s[0, 1] == 255  # used to wrap around to black


def test_log_transform_brightens_dark_tones():
    r = np.array([[10]], dtype=np.uint8)
    assert log_transform(r, c=255 / np.log(256))[0, 0] > 10


def test_power_law_gamma_darkens_or_brightens():
    r = np.array([[0, 128, 255]], dtype=np.uint8)
    darker = power_law_transform(r, gamma=2)
    brighter = power_law_transform(r, gamma=0.5)
    assert darker.tolist() == [[0, 64, 255]]
    assert brighter[0, 1] > 128
    assert power_law_transform(r, gamma=1).tolist() == r.tolist()


def test_histogram_counts_every_pixel():
    img = np.array([[0, 0, 5], [5, 5, 255]], dtype=np.uint8)
    hist = calculate_histogram(img)
    assert hist[0] == 2 and hist[5] == 3 and hist[255] == 1
    assert hist.sum() == img.size


def test_cdf_is_normalised_to_0_255():
    hist = np.zeros(256)
    hist[[10, 20, 30]] = [1, 2, 1]
    cdf, normalized = calculate_cdf(hist)
    assert cdf[-1] == 4
    assert normalized[255] == 255
    assert all(np.diff(normalized.astype(int)) >= 0)


def test_cdf_of_a_single_colour_image_does_not_divide_by_zero():
    hist = np.zeros(256)
    hist[0] = 100  # every pixel black
    _, normalized = calculate_cdf(hist)
    assert normalized.dtype == np.uint8


def test_matching_an_image_to_its_own_histogram_changes_nothing():
    img = np.array([[10, 20], [30, 30]], dtype=np.uint8)
    _, cdf = calculate_cdf(calculate_histogram(img))
    table = create_lookup_table(cdf, cdf)
    assert apply_lookup_table(img, table).tolist() == img.tolist()


def test_lookup_table_picks_the_truly_closest_level():
    # With uint8 maths, 5 - 250 wrapped to 11 and looked closer than 5 - 100.
    source = np.full(256, 5, dtype=np.uint8)
    target = np.full(256, 100, dtype=np.uint8)
    target[200:] = 250
    assert create_lookup_table(source, target)[0] == 0
