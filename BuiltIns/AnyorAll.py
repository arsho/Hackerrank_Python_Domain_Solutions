'''
Title     : Any or All
Subdomain : Built-Ins
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
n = int(input())
ar = list(map(int,input().split()))
ar = sorted(ar)
if(ar[0]<=0):
    print(False)
else:
    chk = False
    for i in ar:
        s = str(i)
        if (s==s[::-1]):
            chk = True
            break
    print(chk)
