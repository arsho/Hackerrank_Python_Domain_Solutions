"""
Title     : XML2 - Find the Maximum Depth
Subdomain : XML
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
xml_str = ""
n = int(input())
for _ in range(n):
    tmp_str = input()
    xml_str = xml_str + tmp_str

import xml.etree.ElementTree as etree

tree = etree.ElementTree(etree.fromstring(xml_str))
root = tree.getroot()
ar = []


def cnt_node(node):
    return max([0] + [cnt_node(child) + 1 for child in node])


cnt = cnt_node(root)
print(cnt)
