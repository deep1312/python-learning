# This is program-22.py
'''Write a Python Program to Find LCM.
Least Common Multiple (LCM):
LCM, or Least Common Multiple, is the smallest multiple that is exactly divisible by two or
more numbers.
Formula:
LCM(𝑎, 𝑏) =
            |𝑎 ⋅ 𝑏|
           GCD(𝑎, 𝑏)
For two numbers a and b, the LCM can be found using the formula:
For more than two numbers, you can find the LCM step by step, taking the LCM of pairs of
numbers at a time until you reach the last pair.
Note: GCD stands for Greatest Common Divisor.
'''

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1<=num2:
    print("LCM of", num1, "and", num2, "is:", lcm(num2, num1))
else:
    print("LCM of", num1, "and", num2, "is:", lcm(num1, num2))
