'''
Title     : Validating and Parsing Email Addresses
Subdomain : Regex and Parsing
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import re, email.utils
n = int(input())
for t in range(n):
    s = input()
    parsed_email = email.utils.parseaddr(s)[1].strip()
    match_result = bool(re.match(r'(^[A-Za-z][A-Za-z0-9\._-]+)@([A-Za-z]+)\.([A-Za-z]{1,3})$',parsed_email))
    if match_result == True:
        print(s)
