'''
Title     : Decorators 2 - Name Directory
Subdomain : Closures and Decorators
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
ar=[]
n=int(raw_input())
for i in range(0,n):
    str_ar=raw_input().strip().split()
    user_name=str_ar[0]+" "+str_ar[1]
    user_age=int(str_ar[2])
    user_sex=str_ar[3]
    user_new_name=""
    if(user_sex=="M"):
        user_new_name="Mr. "+user_name
    else:
        user_new_name="Ms. "+user_name
    ar.append([user_new_name,user_age])

sorted = sorted(ar, key=lambda tup: tup[1])
for i in range(0,n):
    print sorted[i][0]
