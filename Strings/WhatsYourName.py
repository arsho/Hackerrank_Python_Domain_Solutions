"""
Title     : Whats Your Name?
Subdomain : Introduction
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/whats-your-name/problem
"""


def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a, b))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
