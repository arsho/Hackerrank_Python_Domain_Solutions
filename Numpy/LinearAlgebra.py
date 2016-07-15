'''
Title     : Linear Algebra
Subdomain : Numpy
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import numpy
n = int(input())
ar = []
for i in range(n):
    tmp = list(map(float,input().split()))
    ar.append(tmp)
np_ar = numpy.array(ar,float)
print(numpy.linalg.det(np_ar))
