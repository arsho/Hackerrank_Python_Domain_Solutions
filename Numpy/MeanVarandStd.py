'''
Title     : Mean, Var, and Std
Subdomain : Numpy
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import numpy
n,m = map(int,input().split())
ar = []
for i in range(n):
    tmp = list(map(int,input().split()))
    ar.append(tmp)
np_ar = numpy.array(ar)
print(numpy.mean(np_ar,axis=1))
print(numpy.var(np_ar,axis=0))
print(numpy.std(np_ar,axis=None))
