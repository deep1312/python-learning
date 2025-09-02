# This is program-18.py

no_of_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
a, b = 0,1

fibonacci_series = []

for i in range(no_of_terms):
    fibonacci_series.append(a)
    a,b = b , a+b

print(f"The first {no_of_terms} terms of the Fibonacci sequence are: {fibonacci_series}")