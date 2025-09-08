# This is program-34.py
'''
Write a Python Program for array rotation.
'''
def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]
array = [1, 2, 3, 4, 5]
k = 2
print("Array after rotation:", rotate_array(array, k))