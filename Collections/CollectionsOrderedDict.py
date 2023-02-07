"""
Title     : Collections.OrderedDict()
Subdomain : Collections
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
"""

import collections
import re

n = int(input())
item_od = collections.OrderedDict()
for _ in range(n):
    record_list = re.split(r"(\d+)$", input().strip())
    item_name = record_list[0]
    item_price = int(record_list[1])
    item_od[item_name] = (
        item_price if item_name not in item_od else item_od[item_name] + item_price
    )
for i in item_od:
    print(i + str(item_od[i]))
