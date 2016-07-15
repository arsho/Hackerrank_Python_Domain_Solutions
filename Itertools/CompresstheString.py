'''
Title     : Compress the String!
Subdomain : Itertools
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import itertools
s = input().strip()
s_unique_element = list(set(s))
group = []
key = []
for k,g in itertools.groupby(s):
    group.append(list(g))
    key.append(k)
for i in range(len(group)):
    group_length = len(group[i])
    k = int(key[i])
    print(tuple((group_length,k)),end=' ')
