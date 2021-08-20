'''
Title     : Standardize Mobile Number Using Decorators
Subdomain : Closures and Decorators
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
def wrapper(f):
    def fun(l):
        f(['+91 ' + c[-10:-5] + ' ' + c[-5:] for c in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
