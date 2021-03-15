'''
Title     : Eye and Identity
Subdomain : Numpy
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/np-eye-and-identity/problem
'''
import numpy as np
np.set_printoptions(sign=' ')
print(np.eye(*map(int, input().split())))

