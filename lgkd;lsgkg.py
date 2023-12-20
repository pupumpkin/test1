import PIL
from PIL import Image

img = Image.open("task1.jpeg").convert("L")
width = img.size[0]
height = img.size[1]
img = Image.open("task1.jpeg").convert("L")
img.rotate(40, expand = True).show()
img.resize((100,50)).show()
img.resize((width *50, height *20)).show()