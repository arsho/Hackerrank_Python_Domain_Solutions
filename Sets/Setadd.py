'''
Title     : Set .add()
Subdomain : Sets
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
n = int(input())
country_set = set()
for i in range(n):
    country_name = input()
    country_set.add(country_name)
print(len(country_set))
