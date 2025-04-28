"""
Title     : Transpose and Flatten
Subdomain : Numpy
Domain    : Python
Author    : Md Samshad Rahman
Created   : 15 July 2016
Updated   : 25 November 2024
Problem   : https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
"""

import numpy as np


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        row = list(map(int, input().split()))
        arr.append(row)

    np_arr = np.array(arr)
    print(np.transpose(np_arr))
    print(np_arr.flatten())
