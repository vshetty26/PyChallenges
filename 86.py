class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Example Usage
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)
print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
