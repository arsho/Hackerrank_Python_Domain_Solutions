"""
Title     : Array Mathematics
Subdomain : Numpy
Domain    : Python
Author    : Md Samshad Rahman
Created   : 15 July 2016
Updated   : 25 November 2024
Problem   : https://www.hackerrank.com/challenges/np-array-mathematics/problem
"""
import numpy as np


if __name__ == '__main__':
    n, m = map(int, input().split())

    ar1 = np.array([input().split() for _ in range(n)], int)
    ar2 = np.array([input().split() for _ in range(n)], int)

    print(ar1 + ar2)
    print(ar1 - ar2)
    print(ar1 * ar2)
    print(ar1 // ar2)
    print(ar1 % ar2)
    print(ar1 ** ar2)
