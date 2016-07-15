'''
Title     : Calendar Module
Subdomain : Date and Time
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
import datetime
import calendar
m,d,y=map(int,input().split())
input_date = datetime.date(y,m,d)
print(calendar.day_name[input_date.weekday()].upper())
