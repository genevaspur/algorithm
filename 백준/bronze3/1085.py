# https://www.acmicpc.net/problem/1085

x, y, w, h = map(int, input().split())
print(min(-(x - w), -(y - h), x, y))
