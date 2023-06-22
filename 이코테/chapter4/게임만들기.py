from functools import reduce
import math
import sys
import heapq
import time

start_time = time.time()

# map(int, input().split())

def solution():
    result = 1
    keep_move = True
    n, m = map(int, input().split())
    a, b, d = map(int, input().split())
    game_map = []
    for i in range(m):
        game_map.append(list(map(int, input().split())))

    direction = [(0, (0, 1)), (1, (1, 0)), (2, (0, -1)), (3, (-1, 0))]

    game_map[a][b] = 1

    while keep_move:
        sea_count = 0
        # 시작 지점 방문 처리

        # 왼쪽 방향 보기
        d = 3 if d - 1 == -1 else d - 1

        is_done = False
        # 전방 확인
        for _ in range(4):
            for pos in direction:
                if pos[0] == d:
                    is_land = True if game_map[a + pos[1][0]][b + pos[1][1]] == 0 else False
                    if is_land:
                        # 육지면 이동 후 방문 처리
                        a += pos[1][0]
                        b += pos[1][1]
                        game_map[a][b] = 1
                        result += 1
                        is_done = True
                        break
                    else:
                        # 바다면 갯수 누적
                        sea_count += 1
                        # 왼쪽 보기
                        d = 3 if d - 1 == -1 else d - 1
                        break
            if is_done:
                break
            
        # 이동 불가 할 경우
        if sea_count == 4:
            # 방향 유지한 체 뒤로 한칸 이동
            for pos in direction:
                if pos[0] == d:
                    a -= pos[1][0]
                    b -= pos[1][1]
                    if game_map[a][b] == 1:
                        keep_move = False
                    break
    return result

print(solution())


end_time = time.time()
print("time : ", end_time - start_time)