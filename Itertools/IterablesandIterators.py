'''
Title     : Iterables and Iterators
Subdomain : Itertools
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
from itertools import *

n = int(input())
s = str(input())
k = int(input())

pairs = list(combinations(s.split(),k))
count = 0

for pair in pairs:
    if 'a' in pair:
            count += 1

print(count/len(pairs))
