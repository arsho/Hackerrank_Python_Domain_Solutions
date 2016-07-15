'''
Title     : XML2 - Find the Maximum Depth
Subdomain : XML
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
xml_str=""
n=int(raw_input())
for i in range(0,n):
    tmp_str=raw_input()
    xml_str=xml_str+tmp_str
    
import xml.etree.ElementTree as etree
tree = etree.ElementTree(etree.fromstring(xml_str))
root=tree.getroot()
ar=[]
def cnt_node(node):
    return max( [0] + [cnt_node(child)+1 for child in node])
cnt=cnt_node(root)
print cnt
