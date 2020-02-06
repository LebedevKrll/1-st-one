from copy import deepcopy
from PIL import Image
tatras = Image.open("durka.jpg")
(width, height) = tatras.size
for x in range(0, width):
	for y in range( 0, height):
		r = tatras.getpixel((x, y))
		e = deepcopy(r)
		s = (e[0] + e[2] + e[1] - 560) * 2
		tatras.putpixel((x, y), (s, s, s))
tatras.save('top.png')