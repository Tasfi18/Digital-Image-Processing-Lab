from PIL import Image
import numpy as np

image = Image.open('C:/Users/USER/Videos/Captures/TBD/dip lab/demo5.jpg')

gray_image = image.convert('L')

r = np.array(gray_image)

c = 50
gamma = 2
E = 1
s = np.zeros_like(r)
for i in range(r.shape[0]):
    for j in range(r.shape[1]):
        temp_value = c * ((r[i, j] + E) ** gamma)
        if temp_value < 0:
            s[i, j] = 0
        elif temp_value > 255:
            s[i, j] = 255
        else:
            s[i, j] = temp_value

s = s.astype(np.uint8)
s_image = Image.fromarray(s)
s_image.show()
