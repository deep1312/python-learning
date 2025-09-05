# This is program-24.py

'''Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.
How can we manually convert a decimal number to binary, octal and hexadecimal?
Converting a decimal number to binary, octal, and hexadecimal involves dividing the
decimal number by the base repeatedly and noting the remainders at each step. Here's a
simple example:
Let's convert the decimal number 27 to binary, octal, and hexadecimal.
1. Binary:
Divide 27 by 2. Quotient is 13, remainder is 1. Note the remainder.
Divide 13 by 2. Quotient is 6, remainder is 1. Note the remainder.
Divide 6 by 2. Quotient is 3, remainder is 0. Note the remainder.
Divide 3 by 2. Quotient is 1, remainder is 1. Note the remainder.
Divide 1 by 2. Quotient is 0, remainder is 1. Note the remainder.
Reading the remainders from bottom to top, the binary representation of 27 is 11011.
2. Octal:
Divide 27 by 8. Quotient is 3, remainder is 3. Note the remainder.
Divide 3 by 8. Quotient is 0, remainder is 3. Note the remainder.
Reading the remainders from bottom to top, the octal representation of 27 is 33.
3. Hexadecimal:
Divide 27 by 16. Quotient is 1, remainder is 11 (B in hexadecimal). Note the
remainder.
Reading the remainders, the hexadecimal representation of 27 is 1B.
So, in summary:
Binary: 27 in decimal is 11011 in binary.
Octal: 27 in decimal is 33 in octal.
Hexadecimal: 27 in decimal is 1B in hexadecimal.
'''
num = int(input("Enter a decimal number: "))

print(f"Binary of {num} is : {bin(num)[2:]}")
print(f"Octal of {num} is : {oct(num)[2:]}")
print(f"Hexadecimal of {num} is : {hex(num)[2:].upper()}")