'''
Title     : Introduction to Regex Module
Subdomain : Regex and Parsing
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import re
n = int(input())
for i in range(n):
    s = input()    
    search_result = re.search(r'^[+-]?\d*\.\d+$',s)
    print(bool(search_result))
