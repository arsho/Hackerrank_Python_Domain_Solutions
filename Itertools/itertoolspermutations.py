'''
Title     : itertools.permutations()
Subdomain : Itertools
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/itertools-permutations/problem
'''
import itertools
s,n = list(map(str,input().split(' ')))
s = sorted(s)
for p in list(itertools.permutations(s,int(n))):
    print(''.join(p))
