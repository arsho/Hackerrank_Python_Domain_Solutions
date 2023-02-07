"""
Title     : String Formatting
Subdomain : Strings
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/python-string-formatting/problem
"""


n = int(input().strip())
w = len(bin(n)[2:])
for i in range(1, n + 1):
    o = oct(i)[2:]
    h = hex(i)[2:]
    h = h.upper()
    b = bin(i)[2:]
    d = str(i)
    print("{:>{width}} {:>{width}} {:>{width}} {:>{width}}".format(d, o, h, b, width=w))
