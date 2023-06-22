from functools import reduce
import math
import sys
import heapq
from collections import deque
import time

start_time = time.time()

# https://school.programmers.co.kr/learn/courses/30/lessons/43162
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(v):
        visited[v] = True
        for j in range(n):
            if not visited[j] and computers[j][v] == 1:
                dfs(j)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1


    return answer

print(solution(n, computers))

end_time = time.time()
print("time : ", end_time - start_time)
