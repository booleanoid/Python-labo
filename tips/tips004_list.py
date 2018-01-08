#!/usr/bin/env python
# coding: utf-8

list_a = [1, 2, 3, 4, 5]
list_b = list_a # shallow copy
list_c = list_a.copy() # deep copy

list_a[3] = 88
print(list_b[3])
# 88

print(list_c[3])
# 4


fruits = ["strawberry", "orange", "banana", "apple", "grape"]

print(sorted(fruits))
# ['apple', 'banana', 'grape', 'orange', 'strawberry']

print(fruits)
# ['strawberry', 'orange', 'banana', 'apple', 'grape']

fruits.sort()
print(fruits)
# ['apple', 'banana', 'grape', 'orange', 'strawberry']
