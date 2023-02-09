"""
Title     : Collections.deque()
Subdomain : Collections
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/py-collections-deque/problem
"""

import collections

n = int(input())
d = collections.deque()
for _ in range(n):
    cmd = list(input().strip().split())
    opt = cmd[0]
    if opt == "append":
        d.append(int(cmd[1]))
    elif opt == "appendleft":
        d.appendleft(int(cmd[1]))
    elif opt == "pop":
        d.pop()
    elif opt == "popleft":
        d.popleft()
for i in d:
    print(i, end=" ")
