# This is program-20.py

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

list_of_armstrong_numbers = []

for num in range (lower_limit,upper_limit + 1):
    sum = 0
    temp = num
    length_of_num = len(str(num))

    while temp > 0:
        digit = temp % 10
        sum += digit ** length_of_num
        temp //= 10

    if sum == num:
        list_of_armstrong_numbers.append(num)

print(f"Armstrong Numbers between {lower_limit} and {upper_limit} are: {list_of_armstrong_numbers}")

