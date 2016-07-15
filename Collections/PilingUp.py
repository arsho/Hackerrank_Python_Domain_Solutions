'''
Title     : Piling Up!
Subdomain : Collections
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
from collections import deque
cas = int(input())
for t in range(cas):
    n = int(input())
    dq = deque(map(int,input().split()))
    possible = True
    element = (2**31)+1
    while dq:
        left_element = dq[0]
        right_element = dq[-1]
        if left_element>=right_element and element>=left_element:
            element = dq.popleft()
        elif right_element>=left_element and element>=right_element:
            element = dq.pop()
        else:
            possible = False
            break
    if possible:
        print('Yes')
    else:
        print('No')   
