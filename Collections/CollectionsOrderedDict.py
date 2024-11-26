"""
Title     : Collections.OrderedDict()
Subdomain : Collections
Domain    : Python
Author    : Md Samshad Rahman
Created   : 15 July 2016
Updated   : 26 November 2024
Problem   : https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
"""

from collections import OrderedDict


if __name__ == '__main__':
    ordered_dictionary = OrderedDict()

    n = int(input())

    for _ in range(n):
        s = list(input().split())
        price = int(s[len(s) - 1])
        name = ' '.join(s[:len(s) - 1])

        if ordered_dictionary.get(name):
            ordered_dictionary[name] += price
        else:
            ordered_dictionary[name] = price

    for key, value in ordered_dictionary.items():
        print(key, value)
