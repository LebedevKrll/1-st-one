'''Yuy.py code'''

from copy import deepcopy
from PIL import Image
TATRAS = Image.open("durka.jpg")
(WIDTH, HEIGHT) = TATRAS.size
for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        r = TATRAS.getpixel((x, y))
        e = deepcopy(r)
        s = (e[0] + e[2] + e[1] - 560) * 2
        TATRAS.putpixel((x, y), (s, s, s))
TATRAS.save('top.png')
