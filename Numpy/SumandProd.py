"""
Title     : Sum and Prod
Subdomain : Numpy
Domain    : Python
Author    : Md Samshad Rahman
Created   : 15 July 2016
Updated   : 25 November 2024
Problem   : https://www.hackerrank.com/challenges/np-sum-and-prod/problem
"""
import numpy as np


if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = np.array([input().split() for _ in range(n)], int)

    s = np.sum(arr, axis=0)
    print(np.prod(s))
