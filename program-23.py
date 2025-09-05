# This is program-23.py
'''Write a Python Program to Find HCF.
Highest Common Factor(HCF):
HCF, or Highest Common Factor, is the largest positive integer that divides two or more
numbers without leaving a remainder.
Formula:
    HCF(𝑎, 𝑏) = GCD(𝑎, 𝑏)
For two numbers a and b, the HCF can be found using the formula:
For more than two numbers, you can find the HCF by taking the GCD of pairs of numbers at
a time until you reach the last pair.
Note: GCD stands for Greatest Common Divisor.
'''
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

print("HCF of", num1, "and", num2, "is:", gcd(num1, num2))
# HCF is same as GCD