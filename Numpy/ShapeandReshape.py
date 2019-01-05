'''
Title     : Shape and Reshape
Subdomain : Numpy
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/np-shape-reshape/problem
'''
import numpy
ar = list(map(int,input().split()))
np_ar = numpy.array(ar)
print(numpy.reshape(np_ar,(3,3)))
