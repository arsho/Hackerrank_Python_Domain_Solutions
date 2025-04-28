"""
Title     : Zeros and Ones
Subdomain : Numpy
Domain    : Python
Author    : Md Samshad Rahman
Created   : 15 July 2016
Updated   : 25 November 2024
Problem   : https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
"""

import numpy as np


if __name__ == "__main__":
    n_arr = list(map(int, input().split()))
    n = tuple(n_arr)
    print(np.zeros(n, dtype=np.int32))
    print(np.ones(n, dtype=np.int32))
