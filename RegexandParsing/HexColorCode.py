'''
Title     : Hex Color Code
Subdomain : Regex and Parsing
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import re
n = int(input())
for t in range(n):
    s = input()
    match_result = re.findall(r'(#[0-9A-Fa-f]{3}|#[0-9A-Fa-f]{6})(?:[;,.)]{1})',s)
    for i in match_result:
        if i != '':
            print(i)
