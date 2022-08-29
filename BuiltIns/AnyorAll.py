'''
Title     : Any or All
Subdomain : Built-Ins
Domain    : Python
Author    : Ahmedur Rahman Shovon
Updater   : Imtiaz Ahmed
Created   : 15 July 2016
Updated   : 29 August 2022
Problem   : https://www.hackerrank.com/challenges/any-or-all/problem
'''

ar = sorted(input().split())

if ar[0] < 0:
    print(False)
else:
    chk = False
    for i in ar:
        if i == i[::-1]:
            chk = True
            break
    print(chk)