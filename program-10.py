# This is program-10.py

num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))

print(f"Before Swapping: num1 = {num1}, num2 = {num2}")
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"After Swapping: num1 = {num1}, num2 = {num2}")