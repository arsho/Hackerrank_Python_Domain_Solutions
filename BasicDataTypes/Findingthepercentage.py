'''
Title     : Finding the percentage
Subdomain : Data Types
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 06 July 2020
Problem   : https://www.hackerrank.com/challenges/finding-the-percentage/problem
'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    res = sum(student_marks[query_name])/len(student_marks[name])
    print("{:.2f}".format(res))