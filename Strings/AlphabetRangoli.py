"""
Title     : Alphabet Rangoli
Subdomain : Strings
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/alphabet-rangoli/problem
"""

import string
    design = string.ascii_lowercase
    L = []
    for i in range(n):
        s = "-".join(design[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
    print('\n'.join(L[:0:-1]+L))
