'''
Title     : List Comprehensions
Subdomain : Data Types
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(raw_input())
y=int(raw_input())
z=int(raw_input())
n=int(raw_input())
final_ar=[]
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            tmp=i+j+k
            if(tmp!=n):
                ar=[i,j,k]
                final_ar.append(ar)
                
print final_ar
