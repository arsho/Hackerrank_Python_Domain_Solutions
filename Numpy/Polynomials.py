'''
Title     : Polynomials
Subdomain : Numpy
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import numpy
p = numpy.array(list(map(float,input().split())),float)
x = float(input())
print(numpy.polyval(p,x))
