# This is program-31.py
'''Write a Python Program for cube sum of first n natural numbers?
The cube sum of the first n natural numbers is the sum of the cubes of all integers from 1 to n.
Mathematically, it can be expressed as:
    cube_sum(n) = 1^3 + 2^3 + 3^3 + ... + n^3
This can also be calculated using the formula:
    cube_sum(n) = (n * (n + 1) / 2)^2
'''

def cube_sum(n):
    return (n * (n + 1) // 2) ** 2

n = int(input("Enter a positive integer n: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    print("The cube sum of the first", n, "natural numbers is:", cube_sum(n))