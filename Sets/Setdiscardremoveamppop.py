'''
Title     : Set .discard(), .remove() &amp; .pop()
Subdomain : Sets
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
n = int(input())
s = set(map(int, input().split())) 
n = int(input())
for i in range(n):
    cmd = list(input().split(' '))
    if (len(cmd) == 1):
        s.pop()
    else:
        value = int(cmd[1])
        s.discard(value)
print(sum(s))
