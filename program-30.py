# This is program-30.py

'''Write a Python Program to calculate the natural logarithm of any number.
The natural logarithm, often denoted as ln(𝑥), is a mathematical function that represents the
logarithm to the base 𝑒, where 𝑒 is the mathematical constant approximately equal to 2.71828. In other words, for a positive number 𝑥, the natural logarithm of 𝑥 is the exponent 𝑦 that satisfies the equation 𝑒^𝑦 = 𝑥.
Mathematically, the natural logarithm is expressed as:
ln(𝑥)
where 𝑥 is a positive real number.
It is commonly used in various branches of mathematics, especially in calculus and
mathematical analysis, as well as in fields such as physics, economics, and engineering.
The natural logarithm has properties that make it particularly useful in situations involving
exponential growth or decay.
'''
import math

num = float(input("Enter a positive number: "))
if num <= 0:
    print("Natural logarithm is not defined for non-positive numbers.")
else:
    ln_value = math.log(num)
    print("The natural logarithm of", num, "is:", ln_value)