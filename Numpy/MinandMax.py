"""
Title     : Min and Max
Subdomain : Numpy
Domain    : Python
Author    : Md Samshad Rahman
Created   : 15 July 2016
Updated   : 25 November 2024
Problem   : https://www.hackerrank.com/challenges/np-min-and-max/problem
"""
import numpy as np


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = np.array([input().split() for _ in range(n)], int)
    result = np.max(np.min(arr, axis=1))
    print(result)
