"""
Title     : Concatenate
Subdomain : Numpy
Domain    : Python
Author    : Md Samshad Rahman
Created   : 15 July 2016
Updated   : 25 November 2024
Problem   : https://www.hackerrank.com/challenges/np-concatenate/problem
"""

import numpy as np


if __name__ == '__main__':
    n, m, p = map(int, input().split())

    arr1 = []
    arr2 = []
    for _ in range(n):
        tmp = list(map(int, input().split()))
        arr1.append(tmp)
    for _ in range(m):
        tmp = list(map(int, input().split()))
        arr2.append(tmp)
    np_arr1 = np.array(arr1)
    np_arr2 = np.array(arr2)
    print(np.concatenate((np_arr1, np_arr2), axis=0))
