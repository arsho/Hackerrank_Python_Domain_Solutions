"""
Title     : Triangle Quest 2
Subdomain : Math
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/triangle-quest-2/problem
"""
for i in range(
    1, int(input())
):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i - 1) // 9) * i)
