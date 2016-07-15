'''
Title     : Incorrect Regex
Subdomain : Errors and Exceptions
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import re
n = int(input())
for i in range(n):
    s = input()
    try:
        re.compile(s)
        print(True)
    except Exception as e:
        print(False)
