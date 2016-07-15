'''
Title     : Exceptions
Subdomain : Errors and Exceptions
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
n = int(input())
for i in range(n):
    a,b=input().split()
    try:
        print(int(a)//int(b))
    except Exception as e:
        print("Error Code: "+str(e))
