'''
Title     : Mutations
Subdomain : Strings
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
s=raw_input()
in_str_ar=raw_input().strip().split()
pos=int(in_str_ar[0])
c=in_str_ar[1]
final_str=s[:pos]+c+s[pos+1:]
print final_str
