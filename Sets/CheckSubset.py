'''
Title     : Check Subset
Subdomain : Sets
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
    a = int(input()); A = set(input().split()) 
    b = int(input()); B = set(input().split())
    print((A & B) == A)
