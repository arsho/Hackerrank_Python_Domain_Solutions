'''
Title     : Set Mutations
Subdomain : Sets
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
n = int(input())
a = set(map(int,input().split()))
N = int(input())
for i in range(N):
    cmd = input().split()
    opt = cmd[0]
    s = set(map(int,input().split()))
    if (opt == 'update'):
        a |= s
    elif (opt == 'intersection_update'):
        a &= s
    elif (opt == 'difference_update'):
        a -= s
    elif (opt == 'symmetric_difference_update'):
        a ^= s
print(sum(a))
