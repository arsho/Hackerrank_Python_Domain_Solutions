"""
Title     : Arrays
Subdomain : Numpy
Domain    : Python
Author    : Md Samshad Rahman
Created   : 15 July 2016
Updated   : 25 November 2024
Problem   : https://www.hackerrank.com/challenges/np-arrays/problem
"""

import numpy

def arrays(arr):
    np_ar = numpy.array(arr, float)
    return np_ar[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
