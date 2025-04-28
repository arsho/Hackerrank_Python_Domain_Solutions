"""
Title     : Floor, Ceil and Rint
Subdomain : Numpy
Domain    : Python
Author    : Md Samshad Rahman
Created   : 15 July 2016
Updated   : 25 November 2024
Problem   : https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
"""

import numpy as np


if __name__ == "__main__":
    np.set_printoptions(legacy="1.13")
    arr = np.array(input().split(), float)
    print(np.floor(arr))
    print(np.ceil(arr))
    print(np.rint(arr))

    # Alternate solution
    # print(*(f(A) for f in [np.floor, np.ceil, np.rint]), sep='\n')
