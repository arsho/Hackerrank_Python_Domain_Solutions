"""
Title     : Zipped!
Subdomain : Built-Ins
Domain    : Python
Author    : Ahmedur Rahman Shovon
Updater   : Imtiaz Ahmed
Created   : 15 July 2016
Updated   : 30 August 2022
Problem   : https://www.hackerrank.com/challenges/zipped/problem
"""

N, X = map(int, input().split())
scores = []
for _ in range(X):
    scores.append(list(map(float, input().split())))
for i in zip(*scores):
    print(sum(i) / len(i))
