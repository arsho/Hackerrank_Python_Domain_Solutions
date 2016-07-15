'''
Title     : Collections.OrderedDict()
Subdomain : Collections
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import collections, re
n = int(input())
item_od = collections.OrderedDict()
for i in range(n):
    record_list = re.split(r'(\d+)$',input().strip())
    item_name = record_list[0]
    item_price = int(record_list[1])
    if item_name not in item_od:
        item_od[item_name]=item_price
    else:
        item_od[item_name]=item_od[item_name]+item_price
            
for i in item_od:
    print(i+str(item_od[i]))
