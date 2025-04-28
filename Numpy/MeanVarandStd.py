"""
Title     : Mean, Var, and Std
Subdomain : Numpy
Domain    : Python
Author    : Md Samshad Rahman
Created   : 15 July 2016
Updated   : 25 November 2024
Problem   : https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
"""

import numpy as np


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = np.array([input().split() for _ in range(n)], int)

    print(np.mean(arr, axis=1))
    print(np.var(arr, axis=0))
    print(round(np.std(arr, axis=None), 11))
