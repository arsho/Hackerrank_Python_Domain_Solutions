'''
Title     : Re.split()
Subdomain : Regex and Parsing
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/re-split/problem
'''
import re;[print(i) for i in re.split("[,\.]?",input().strip()) if i]
