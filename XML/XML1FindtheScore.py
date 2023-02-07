'''
Title     : XML 1 - Find the Score
Subdomain : XML
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/xml-1-find-the-score/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
xml_str=""
n=int(input())
for _ in range(n):
    tmp_str=input()
    xml_str=xml_str+tmp_str

cnt=xml_str.count("='")
xml_str=""
print (cnt)
