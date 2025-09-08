# This is program-28.py
'''
Write a Python Program to Find Factorial of Number Using Recursion.
The factorial of a non-negative integer ( n ) is the product of all positive integers less than or
equal to ( n ). It is denoted by ( n! ) and is defined as:
    𝑛! = 𝑛 × (𝑛 − 1) × (𝑛 − 2) × … × 3 × 2 × 1
For example:
    5! = 5 × 4 × 3 × 2 × 1 = 120
The factorial of 0 ( 0! ) is defined to be 1.
Factorials are commonly used in mathematics, especially in combinatorics and probability,
to count the number of ways a set of elements can be arranged or selected.
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input("Enter a non-negative integer: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", num, "is", factorial(num))