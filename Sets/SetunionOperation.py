'''
Title     : Set .union() Operation
Subdomain : Sets
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/py-set-union/problem
'''
n = input()
eng = set(map(int,input().split()))
b = input()
fre = set(map(int,input().split()))
print(len(eng.union(fre)))
