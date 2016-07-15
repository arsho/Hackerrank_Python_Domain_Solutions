'''
Title     : Floor, Ceil and Rint
Subdomain : Numpy
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import numpy
np_ar = numpy.array(list(map(float,input().split())),float)
print(numpy.floor(np_ar))
print(numpy.ceil(np_ar))
print(numpy.rint(np_ar))
