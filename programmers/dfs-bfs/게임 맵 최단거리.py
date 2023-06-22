from functools import reduce
import math
import sys
import heapq
from collections import deque
import time

start_time = time.time()

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    answer = bfs(0, 0, n, m, maps)

    return answer


def bfs(x, y, n, m, maps):
    queue = deque()
    queue.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵 벗어남
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽
            if maps[nx][ny] == 0:
                continue

            # 미방문
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    return -1 if maps[n - 1][m - 1] == 1 else maps[n - 1][m - 1]


print(solution(maps))

end_time = time.time()
print("time : ", end_time - start_time)
