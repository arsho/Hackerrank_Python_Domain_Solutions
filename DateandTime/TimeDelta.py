'''
Title     : Time Delta
Subdomain : Date and Time
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/python-time-delta/problem
'''
import datetime
cas = int(input())
for t in range(cas):
    timestamp1 = input().strip()
    timestamp2 = input().strip()
    time_format = "%a %d %b %Y %H:%M:%S %z"
    time_second1 = datetime.datetime.strptime(timestamp1,time_format)
    time_second2 = datetime.datetime.strptime(timestamp2,time_format)
    print(int(abs((time_second1-time_second2).total_seconds())))

    
    
##    -------updated code----------

import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    timestamp1 = t1.strip()
    timestamp2 = t2.strip()
    time_format = "%a %d %b %Y %H:%M:%S %z"
    time_second1 = datetime.strptime(timestamp1,time_format)
    time_second2 = datetime.strptime(timestamp2,time_format)
    print(int(abs((time_second1-time_second2).total_seconds())))
    return (int(abs((time_second1-time_second2).total_seconds())))
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(int(delta)) + '\n')

    fptr.close()
