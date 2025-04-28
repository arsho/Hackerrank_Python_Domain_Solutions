"""
Title     : Shape and Reshape
Subdomain : Numpy
Domain    : Python
Author    : Md Samshad Rahman
Created   : 15 July 2016
Updated   : 25 November 2024
Problem   : https://www.hackerrank.com/challenges/np-shape-reshape/problem
"""

import numpy as np


if __name__ == "__main__":
    array = list(map(int, input().split()))
    np_arr = np.array(array)
    print(np.reshape(np_arr, (3, 3)))
