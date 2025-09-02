# This is program-19.py

num = int(input("Enter the number which need to is armstrong: "))

sum = 0
temp = num
length_of_num = len(str(num))

if num < 0:
    print("please Enter positive number")
else:
    while temp > 0:
        digit = temp % 10
        sum += digit ** length_of_num
        temp //= 10

if sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")