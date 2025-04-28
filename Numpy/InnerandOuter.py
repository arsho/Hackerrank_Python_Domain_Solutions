"""
Title     : Inner and Outer
Subdomain : Numpy
Domain    : Python
Author    : Md Samshad Rahman
Created   : 15 July 2016
Updated   : 25 November 2024
Problem   : https://www.hackerrank.com/challenges/np-inner-and-outer/problem
"""
import numpy as np


if __name__ == '__main__':
    arr1 = np.array(list(map(int, input().split())))
    arr2 = np.array(list(map(int, input().split())))

    print(np.inner(arr1, arr2))
    print(np.outer(arr1, arr2))
