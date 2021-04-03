'''
Title     : Input()
Subdomain : Built-Ins
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Updated   : 3 April 2021
Problem   : https://www.hackerrank.com/challenges/input/problem
'''

if __name__ == "__main__":
    x, k = map(int, input().strip().split())
    string = input().strip()
    
    if eval(string) == k:
        print(True)
    else:
        print(False)
