'''
Title     : Floor, Ceil and Rint
Subdomain : Numpy
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
'''
import numpy as np
np.set_printoptions(sign=' ')
a = np.array(input().split(), float)
print(*(f(a) for f in [np.floor, np.ceil, np.rint]), sep='\n')
