'''
Title     : XML 1 - Find the Score
Subdomain : XML
Domain    : Python
Author    : Aditya Prakash Gupta
Created   : 20 August 2021
Problem   : https://www.hackerrank.com/challenges/xml-1-find-the-score/problem
'''
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    return len(node.attrib) + sum(get_attr_number(child) for child in node)

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
