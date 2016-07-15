'''
Title     : Dot and Cross
Subdomain : Numpy
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import numpy
n = int(input())
ar1 = []
ar2 = []
for i in range(n):
    tmp = list(map(int,input().split()))
    ar1.append(tmp)
np_ar1 = numpy.array(ar1)
for i in range(n):
    tmp = list(map(int,input().split()))
    ar2.append(tmp)
np_ar2 = numpy.array(ar2)
print(numpy.dot(np_ar1,np_ar2))
