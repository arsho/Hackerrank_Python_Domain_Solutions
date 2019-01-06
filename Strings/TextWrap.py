'''
Title     : Text Wrap
Subdomain : Strings
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/text-wrap/problem
'''
import textwrap
s = input()
w = int(input().strip())
print(textwrap.fill(s,w))
