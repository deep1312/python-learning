# This is program-9.py

import math

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Roots are real and different: {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"Roots are real and the same: {root}")
elif discriminant < 0:
    realPart = -b / (2*a)
    imaginaryPart = math.sqrt(-discriminant) / (2*a)
    print(f"Roots are complex and different: {realPart} + {imaginaryPart}i and {realPart} - {imaginaryPart}i")
    