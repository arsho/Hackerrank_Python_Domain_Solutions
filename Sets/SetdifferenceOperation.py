'''
Title     : Set .difference() Operation
Subdomain : Sets
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
e = int(input())
eng = set(map(int,input().split())) 
f = int(input())
fre = set(map(int,input().split()))
print(len(eng - fre))
