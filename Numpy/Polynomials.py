"""
Title     : Polynomials
Subdomain : Numpy
Domain    : Python
Author    : Md Samshad Rahman
Created   : 15 July 2016
Updated   : 25 November 2024
Problem   : https://www.hackerrank.com/challenges/np-polynomials/problem
"""
import numpy as np


if __name__ == '__main__':
    p = np.array(list(map(float, input().split())), float)
    x = float(input())
    print(np.polyval(p, x))
