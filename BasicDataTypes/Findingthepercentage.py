'''
Title     : Finding the percentage
Subdomain : Data Types
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/finding-the-percentage/problem
'''
# Given
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

# Enter your code here. Read input from STDIN. Print output to STDOUT
a=float(sum(student_marks.get(query_name))/len(student_marks.get(query_name)))
print('%.2f'%a)


