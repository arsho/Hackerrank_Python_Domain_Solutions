"""
Title     : Eye and Identity
Subdomain : Numpy
Domain    : Python
Author    : Md Samshad Rahman
Created   : 15 July 2016
Updated   : 25 November 2024
Problem   : https://www.hackerrank.com/challenges/np-eye-and-identity/problem
"""

import numpy as np


if __name__ == '__main__':
    np.set_printoptions(legacy="1.13")
    n, m = map(int, input().split())
    print(np.eye(n, m, k=0))
