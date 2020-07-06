'''
Title     : List Comprehensions
Subdomain : Data Types
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 06 July 2020
Problem   : https://www.hackerrank.com/challenges/list-comprehensions/problem
'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ar = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
    print(ar)