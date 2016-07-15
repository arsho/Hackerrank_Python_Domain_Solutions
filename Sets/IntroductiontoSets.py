'''
Title     : Introduction to Sets
Subdomain : Sets
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
n = input()
ar = map(int,input().split(' '))
ar=set(ar)
print(sum(ar) / len(ar))
