"""
Title     : ginortS
Subdomain : Built-Ins
Domain    : Python
Author    : Ahmedur Rahman Shovon
Updater   : Imtiaz Ahmed
Created   : 15 July 2016
Updated   : 29 August 2022
Problem   : https://www.hackerrank.com/challenges/ginorts/problem
"""

s = input()
print(
    "".join(
        sorted(
            s,
            key=lambda x: (
                x.isdigit() and int(x) % 2 == 0,
                x.isdigit(),
                x.isupper(),
                x.islower(),
                x,
            ),
        )
    )
)
