"""
Title     : collections.Counter()
Subdomain : Collections
Domain    : Python
Author    : Md Samshad Rahman
Created   : 15 July 2016
Updated   : 26 November 2024
Problem   : https://www.hackerrank.com/challenges/collections-counter/problem
"""
import collections


if __name__ == '__main__':
    total_shoes = int(input())
    shoe_sizes = list(map(int, input().split()))
    inventory = collections.Counter(shoe_sizes)

    total_customers = int(input())
    total_revenue = 0

    for _ in range(total_customers):
        size, price = map(int, input().split())
        if inventory.get(size) and inventory[size] > 0:
            total_revenue += price
            inventory[size] -= 1

    print(total_revenue)


