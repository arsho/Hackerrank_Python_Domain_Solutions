'''
Title     : Standardize Mobile Number Using Decorators
Subdomain : Closures and Decorators
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
ar=[]
for i in range(0,n):
    tmp_str=raw_input()
    tmp_str=tmp_str[len(tmp_str)-10:]
    ar.append(tmp_str)
    
ar.sort()
for i in range(0,len(ar)):
    print "+91 "+ar[i][:5]+" "+ar[i][5:]
