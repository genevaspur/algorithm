# https://www.acmicpc.net/problem/2845
l, p = map(int, input().split())
arr = list(map(int, input().split()))
num = l * p
answer = []

for i in arr:
    answer.append(i - num)

for i in answer:
    print(i, end=' ')
