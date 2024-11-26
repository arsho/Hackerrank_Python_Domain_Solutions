"""
Title     : Dot and Cross
Subdomain : Numpy
Domain    : Python
Author    : Md Samshad Rahman
Created   : 15 July 2016
Updated   : 25 November 2024
Problem   : https://www.hackerrank.com/challenges/np-dot-and-cross/problem
"""
import numpy as np


if __name__ == '__main__':
    n = int(input())

    arr1 = np.array([input().split() for _ in range(n)], int)
    arr2 = np.array([input().split() for _ in range(n)], int)

    print(np.dot(arr1, arr2))
