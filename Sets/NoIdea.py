'''
Title     : No Idea!
Subdomain : Sets
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
from collections import Counter
n, m = map(int,input().split())
ar = list(map(int,input().split()))
ar_set = set(ar)
ar_counter = Counter(ar)
set_a = set(map(int,input().split()))
set_b = set(map(int,input().split()))
intersect_ar_a = list(ar_set&set_a)
intersect_ar_b = list(ar_set&set_b)
result = 0
for element in intersect_ar_a:
    result += ar_counter[element]
for element in intersect_ar_b:
    result -= ar_counter[element]
    
print(result)
