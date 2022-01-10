import math

"""
The following Complex number class used to represent complex numbers in Python.
A complex number objects consists of the fields a and b, where a and b
correspond to the real and imaginary parts of the complex number. The class
includes methods methods for comparing and performing arithmetic operations on
complex numbers.
"""

class Complex:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        if self.b>0:
            return "{}+{}i".format(self.a, self.b)
        elif self.b<0:
            self.b=-self.b
            return "{}-{}i".format(self.a, self.b)
        elif self.b == 0:
            return "{}".format(self.a)
        elif self.a == 0:
            return "{}i".format(self.b)
    def __repr__(self):
        if self.b>0:
            return "'{}+{}i'".format(self.a, self.b)
        elif self.b<0:
            self.b=-self.b
            return "'{}-{}i'".format(self.a, self.b)
        elif self.b == 0:
            return "'{}'".format(self.a)
        elif self.a == 0:
            return "'{}i'".format(self.b)
    def __add__(self, other):
        if type(other) == int:
            other = Complex(other, 0)
        return Complex(self.a+other.a, self.b+other.b)
    def __radd__(self, other):
        if type(other) == int:
            other = Complex(other, 0)
        return Complex(self.a+other.a, self.b+other.b)
    def __sub__(self, other):
        if type(other) == int:
            other = Complex(other, 0)
        return Complex(self.a-other.a, self.b-other.b)
    def __rsub__(self, other):
        if type(other) == int:
            other = Complex(other, 0)
        return Complex(-self.a+other.a, -self.b+other.b)
    def __mul__(self, other):
        if type(other) == int:
            other = Complex(other, 0)
        return Complex(self.a*other.a - self.b*other.b  , self.a*other.b+self.b*other.a)
    def __rmul__(self, other):
        if type(other) == int:
            other = Complex(other, 0)
        return Complex(self.a*other.a - self.b*other.b  , self.a*other.b+self.b*other.a)
    def __truediv__(self, other):
        if type(other) == int:
            other = Complex(other, 0)
        if other.a==0 and other.b==0:
            return "Undefined!"
        else:
            bottom=other.a*other.a+other.b*other.b
            return Complex((self.a*other.a-self.b*other.b)/bottom,(-self.a*other.b+self.b*other.a)/bottom)
    def __rtruediv__(self, other):
        if type(other) == int:
            other = Complex(other, 0)
        if other.a==0 and other.b==0:
            return "Undefined!"
        else:
            bottom=self.a*self.a+self.b*self.b
            return Complex((self.a*other.a-self.b*other.b)/bottom,(-other.a*self.b+other.b*self.a)/bottom)
    def __eq__(self, other):
        if type(other) == int:
            other = Complex(other, 0)
        return self.a==other.a and self.b==other.b
    def __ne__(self, other):
        if type(other) == int:
            other = Complex(other, 0)
        return self.a!=other.a and self.b!=other.b
    def abs(self):
        return math.sqrt(self.a*self.a+self.b*self.b)
    def __pow__(self, other):
        x = self
        for i in range(1, other):
            self *= x
        return self
