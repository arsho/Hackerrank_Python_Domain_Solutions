"""
Title     : Linear Algebra
Subdomain : Numpy
Domain    : Python
Author    : Md Samshad Rahman
Created   : 15 July 2016
Updated   : 25 November 2024
Problem   : https://www.hackerrank.com/challenges/np-linear-algebra/problem
"""
import numpy as np


if __name__ == '__main__':
    np.set_printoptions(legacy="1.13")
    n = int(input())
    array = np.array([input().split() for _ in range(n)], float)
    print(np.linalg.det(array))
