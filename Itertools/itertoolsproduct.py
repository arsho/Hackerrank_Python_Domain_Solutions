'''
Title     : itertools.product()
Subdomain : Itertools
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/itertools-product/problem
'''
import itertools
ar1 = list(map(int,input().split()))
ar2 = list(map(int,input().split()))
cross = list(itertools.product(ar1,ar2))
for i in cross:
    print(i,end=' ')
