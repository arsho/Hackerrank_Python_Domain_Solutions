'''
Title     : Collections.deque()
Subdomain : Collections
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import collections
n = int(input())
d = collections.deque()
for i in range(n):
    cmd = list(input().strip().split())
    opt = cmd[0]
    if opt == 'pop':
        d.pop()
    elif opt == 'popleft':
        d.popleft()
    elif opt == 'append':
        d.append(int(cmd[1]))
    elif opt == 'appendleft':
        d.appendleft(int(cmd[1]))
for i in d:
    print(i,end=' ')

        
