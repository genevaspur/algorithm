from functools import reduce
import math
import sys
import heapq
from collections import deque
import time

start_time = time.time()

# https://school.programmers.co.kr/learn/courses/30/lessons/43163

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

# [
# ['h', 'o', 't'],
# ['d', 'o', 't'],
# ['d', 'o', 'g'],
# ['l', 'o', 't'],
# ['l', 'o', 'g'],
# ['c', 'o', 'g']
# ]
def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    visited = [False] * len(words)

    q = deque()
    q.append([0, begin])

    while q:
        idx, temp_word = q.popleft()

        if temp_word == target:
            answer = idx
            break

        for i in range(len(words)):
            if not visited[i]:
                count = 0
                for j in range(len(words[i])):
                    if temp_word[j] != words[i][j]:
                        count += 1
                if count == 1:
                    visited[i] = True
                    q.append([idx + 1, words[i]])

    return answer


print(solution(begin, target, words))

end_time = time.time()
print("time : ", end_time - start_time)
