'''
Title     : Eye and Identity
Subdomain : Numpy
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Updated   : 17 March 2021
Problem   : https://www.hackerrank.com/challenges/np-eye-and-identity/problem
'''
import numpy as p
np.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
print(np.eye(n, m, k=0))

