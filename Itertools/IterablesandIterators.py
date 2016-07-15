'''
Title     : Iterables and Iterators
Subdomain : Itertools
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import itertools
n = int(input())
s_ar = input().strip().split()
s = ''.join(s_ar)
k = int(input())
combination = list(itertools.combinations(s,k))
combination_count = len(combination)
a_count = 0

for single_combination in combination:
    if 'a' in single_combination:
        a_count += 1
print(a_count / combination_count)
