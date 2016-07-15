'''
Title     : Symmetric Difference
Subdomain : Sets
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(raw_input())
set_a_str_ar=raw_input().strip().split()
set_a_ar=list(map(int,set_a_str_ar))
n=int(raw_input())
set_b_str_ar=raw_input().strip().split()
set_b_ar=list(map(int,set_b_str_ar))

set_a_set=set(set_a_ar)
set_b_set=set(set_b_ar)
set_a_dif_set=set_a_set.difference(set_b_set)
set_b_dif_set=set_b_set.difference(set_a_set)
res_set=set_a_dif_set.union(set_b_dif_set)
res_ar=list(res_set)
res_ar.sort()
for i in res_ar:
    print i
