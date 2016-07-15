'''
Title     : itertools.combinations()
Subdomain : Itertools
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
from itertools import *
s,n = input().split()
n = int(n) + 1
s = sorted(s)
for i in range(1,n):
    for j in combinations(s,i):
        print(''.join(j))
