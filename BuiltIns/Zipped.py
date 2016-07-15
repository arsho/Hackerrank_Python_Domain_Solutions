'''
Title     : Zipped!
Subdomain : Built-Ins
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
n, x = map(int,input().split())
ar = [0 for i in range(n)]
for i in range(x):
    temp_ar=list(map(float,input().split()))
    for j in range(n):
        ar[j] += temp_ar[j]
for i in range(n):
    print(ar[i]/x)
