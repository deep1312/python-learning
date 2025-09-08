# This is program-35.py

'''Write a Python Program to Split the array and add the first part to the end?
Given an array, the task is to split the array into two parts and add the first part to the end of the second part.
For example, if the input array is [1, 2, 3, 4, 5] and the position to split is 2, then the output should be [3, 4, 5, 1, 2].'''

def split_and_add(arr, pos):
    if pos < 0 or pos > len(arr):
        return "Invalid position"
    return arr[pos:] + arr[:pos]

array = [1, 2, 3, 4, 5]
position = 2
print("Array after split and add:", split_and_add(array, position))