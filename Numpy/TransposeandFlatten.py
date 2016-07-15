'''
Title     : Transpose and Flatten
Subdomain : Numpy
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import numpy
n,m = map(int,input().split())
ar = []
for i in range(n):
    row = list(map(int,input().split()))
    ar.append(row)

np_ar = numpy.array(ar)
print(numpy.transpose(np_ar))
print(np_ar.flatten())
