"""
Title     : Standardize Mobile Number Using Decorators
Subdomain : Closures and Decorators
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
ar = []
for _ in range(n):
    tmp_str = input()
    tmp_str = tmp_str[len(tmp_str) - 10 :]
    ar.append(tmp_str)

ar.sort()
for item in ar:
    print(f"+91 {item[:5]} {item[5:]}")
