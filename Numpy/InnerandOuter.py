'''
Title     : Inner and Outer
Subdomain : Numpy
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import numpy
np_ar1 = numpy.array(list(map(int,input().split())))
np_ar2 = numpy.array(list(map(int,input().split())))
print(numpy.inner(np_ar1,np_ar2))
print(numpy.outer(np_ar1,np_ar2))
