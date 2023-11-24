from math import exp, e
from PIL import Image

class Filter:
    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        raise NotImplementedError

    def apply_to_image(self, img: Image.Image) -> Image.Image:
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = img.getpixel((i, j))
                new_colors = self.apply_to_pixel(r, g, b)
                img.putpixel((i, j), new_colors)
        return img


class RedFilter(Filter):

    def __init__(self):
        self.name = "Red"

    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        r = int(exp(r / 255) / e * 255)
        return r, g, b


class GreenFilter(Filter):

    def __init__(self):
        self.name = "Green"

    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:

        g = int(exp(g / 255) / e * 255)
        return r, g, b


class InverseFilter(Filter):

    def __init__(self):
        self.name = "Inverse"

    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        result = []
        for color in (r, g, b):
            result.append(int((1 - exp(color / 255) / e) * 255))
        return tuple(result)
