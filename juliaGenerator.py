from PIL import Image
from numpy import array
from complex import Complex

"""
The following function is used to determin whether the seed (x,y) is an escapee
of prisoner for a set C value in the iterative function zn+1 = zn**deg + C for a
specified degree 'deg'. We iterate the function 50 times, and if after the
iterations the magnitude of z is less than 2, the seed (x,y) is a prisoner and
the C value is colored black in the image; otherwise, it is colored with a
wavelength that corresponds to how fast the seed escapes (brighter red -> faster
escape).
"""

def juliaSetColor(x, y, a, b, deg):
    c = Complex(a, b)
    z = Complex(x, y)
    for i in range(1, 50):
        if Complex.abs(z) > 2:
            return (int(255 * (i / 50)), 0, 0)
        z = z**deg + c
    return (0, 0, 0)

"""
The following function generates the julia set of the funtion zn+1 = zn**deg + C
for a specified degree 'deg' and complex C value. The function iterates through
each pixel of the image, each which represents a different seed, and uses the
juliaSetColor function to color the pixel accordingly.
"""

def createJuliaSet(a, b, deg):
    w = 700
    mandelbrot = Image.new('RGB', (w, w))
    pixels = mandelbrot.load()
    for x in range(mandelbrot.size[0]):
        print("%.f %%" % (x / w * 100), end="\r")
        for y in range(mandelbrot.size[1]):
            pixels[x, y] = juliaSetColor((x - (0.5 * w)) / (w / 4), (y - (w / 2)) / (w / 4), a, 0-b, deg)
    mandelbrot.show()

"""
Example julia set:
"""

createJuliaSet(0.295, 0.55, 2)
