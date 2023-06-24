"""
Title     : Mean, Var, and Std
Subdomain : Numpy
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
"""

import numpy
nm = input()
inm = nm.split( )
inn = []
for i in inm:
    i = int(i)
    inn.append(i)

arr = []

for i in range(0, inn[0]):
    a = input()
    k = []
    b = a.split(" ")

    for i in b:
        i = int(i)
        k.append(i)
    arr.append(k)

arn = numpy.array(arr)
print(numpy.mean(arn, axis=1))
print(numpy.var(arn, axis=0))
z = numpy.std(arn, axis=None)
j = round(z, 11)
print(j)
