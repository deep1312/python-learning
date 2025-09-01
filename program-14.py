# This is program-14.py

num = int(input("Enter a number: "))

flag = False

if num == 1 :
    print(f"{num} is neither prime nor composite")
else:
    for i in range (2,num//2):
        print(f"{i} starts")
        if num % i == 0 :
            flag = True
            print(f"{i} starts and flag is set to True")
        break

    if flag:
        print(f"{num} is not prime")
    else:
        print(f"{num} is prime")