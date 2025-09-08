# This is program-33.py

'''Write a Python Program to find largest element in an array.'''

def find_largest(arr):
    if not arr:
        return None
    largest = arr[0]
    if len(arr) == 1:
        return largest
    for num in arr[1:]:
        if num > largest:
            largest = num
    return largest

array = [3, 5, 7, 2, -8, -1]
print("The largest element in the array is:", find_largest(array))