"""
Title     : Any or All
Subdomain : Built-Ins
Domain    : Python
Author    : Ahmedur Rahman Shovon
Updater   : Imtiaz Ahmed
Created   : 15 July 2016
Updated   : 29 August 2022
Problem   : https://www.hackerrank.com/challenges/any-or-all/problem
"""

n = input()
ar = input().split()
print(all(int(i) > 0 for i in ar) and any(i == i[::-1] for i in ar))
