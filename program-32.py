# This is program-32.py
'''
Write a Python Program to find sum of array.
In Python, an array is a data structure used to store a collection of elements, each identified
by an index or a key. Unlike some other programming languages, Python does not have a
built-in array type. Instead, the most commonly used array-like data structure is the list.
A list in Python is a dynamic array, meaning it can change in size during runtime. Elements
in a list can be of different data types, and you can perform various operations such as
adding, removing, or modifying elements. Lists are defined using square brackets [] and
can be indexed and sliced to access specific elements or sublists.
Example of a simple list in Python:
my_list = [1, 2, 3, 4, 5]
'''

def sum_of_array(arr):
    return sum(arr)

array = [1, 2, 3, 4, 5]
print("The sum of the array is:", sum_of_array(array))