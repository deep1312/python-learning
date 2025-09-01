# This is program-16.py

factorial = int(input("Enter a number to calculate its factorial: "))

result = 1
for i in range(1, factorial + 1):
    result = result * i
print(f"The factorial of {factorial} is {result}")