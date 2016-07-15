'''
Title     : Write a function
Subdomain : Introduction
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
def is_leap(year):
    leap = False
    if (year % 400 == 0):
        leap = True
    elif year % 4 == 0 and year % 100 !=0:
        leap = True    
    return leap
