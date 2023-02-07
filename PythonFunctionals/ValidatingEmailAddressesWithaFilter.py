"""
Title     : Validating Email Addresses With a Filter
Subdomain : Python Functionals
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
ar = []
for _ in range(n):
    s = input()
    if t := re.search(r"^[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$", s):
        ar.append(s)
ar.sort()

print(ar)
