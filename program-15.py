# This is program-15.py

num = int(input("Enter range: "))

prime_numbers = []

for i in range (1,num+1):
    if i == 1 :
        continue
    else:
        for j in range (2,i):
            # print(f"{j} starts")
            if i % j == 0 :
                break
        else:
            prime_numbers.append(i)
print(f"Prime numbers are: {prime_numbers}")            