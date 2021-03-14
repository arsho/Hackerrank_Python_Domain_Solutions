'''
Title     : Python If-Else
Subdomain : Introduction
Domain    : Python
Author    : Utkarsh Mishra
Created   : 27 Jan 2021
Problem   : https://www.hackerrank.com/challenges/py-if-else/problem
'''
#!/bin/python3

import sys

n = int(input())
if n%2==1 or n in range (5,21):
    print("Weird")
else:
    print("Not Weird")

    
