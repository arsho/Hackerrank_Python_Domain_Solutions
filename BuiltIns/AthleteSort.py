'''
Title     : Athlete Sort
Subdomain : Built-Ins
Domain    : Python
Author    : Atharva Shah
Created   : 3 April 2021
Problem   : https://www.hackerrank.com/challenges/python-sort-sort/problem
'''

import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = []
    for arr_i in range(n):
       arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
       arr.append(arr_t)
    k = int(input().strip())
    
    sorted_arr = sorted(arr, key = lambda x : x[k])
    for row in sorted_arr:
        print(' '.join(str(y) for y in row))
