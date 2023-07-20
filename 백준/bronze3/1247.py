# https://www.acmicpc.net/problem/1247

from sys import stdin

for _ in range(3):
    n = int(stdin.readline())
    total = 0
    for i in range(n):
        total += int(stdin.readline())
    if total == 0:
        print(0)
    else:
        print("+" if total > 0 else "-")
