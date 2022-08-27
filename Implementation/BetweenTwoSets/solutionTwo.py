"""
Title     : Between Two Sets
Subdomain : Implementation
Domain    : Python
Author    : 
Created   : 27 August 2022
Problem   : https://www.hackerrank.com/challenges/between-two-sets/problem
"""

def getTotalX(a, b):
    res = 0

    for i in range(1, 101):
        flag = True
        for num_a in a:
            if i % num_a != 0:
                flag = False
                break
        if flag:
            for num_b in b:
                if num_b % i != 0:
                    flag = False
                    break
        if flag:
            res += 1

    return res 