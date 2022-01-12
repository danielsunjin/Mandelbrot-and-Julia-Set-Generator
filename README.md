# Mandelbrot-and-Julia-Set-Generator
The code in this repository includes my custom complex number Python class and code to generate [Mandelbrot](https://en.wikipedia.org/wiki/Mandelbrot_set) and [Julia](https://en.wikipedia.org/wiki/Julia_set) sets using the class in Python. 

The Mandelbrot set is the set of complex numbers *c = x + yi* for which the function *f(z) = z^deg + c* does not diverge to infinity for some degree *deg* and the seed value *z = 0 + 0i*. The complex numbers that diverge and are part of the Mandelbrot set are called prisoners and the compelx numbers that do diverge are called escapees. The Mandelbrot set can be plotted on the complex plane, with the X and Y axes corresponding to the real and imaginary parts of *c* respectively. This plot is a fractal image. 

The Julia set is the set of complex numbers *z = x + yi* for which the function *f(z) = z^deg + c* does not diverge to infinity for some degree *deg* and a specific complex number *c = a + bi*. The Julia set also results in a fractal image when plotted on the complex plane.

This project was inspired by the GeekForGeeks article [Mandelbrot Fractal Set visualization in Python](https://www.geeksforgeeks.org/mandelbrot-fractal-set-visualization-in-python/).

Python libraries required to run the code:
- PIL
- numpy

**Example Generated Mandelbrot Set:**
![Mandelbrot Set Example](https://github.com/danielsunjin/Mandelbrot-and-Julia-Set-Generator/blob/main/mandelbrot_set_example.PNG)

**Example Generated Julia Set:**
![Julia Set Example](https://github.com/danielsunjin/Mandelbrot-and-Julia-Set-Generator/blob/main/julia_set_example.PNG)
