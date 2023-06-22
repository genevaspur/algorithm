from functools import reduce
import math
import sys
import heapq
from collections import deque
import time

start_time = time.time()

numbers = [1, 1, 1, 1, 1]
target = 3


def solution(numbers, target):
    answer = 0

    def dfs(idx, sum):
        nonlocal answer
        if idx == len(numbers):
            if sum == target:
                answer += 1
        else:
            dfs(idx + 1, sum + numbers[idx])
            dfs(idx + 1, sum - numbers[idx])

    dfs(0, 0)

    return answer


print(solution(numbers, target))

end_time = time.time()
print("time : ", end_time - start_time)
