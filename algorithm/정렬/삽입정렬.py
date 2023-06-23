from functools import reduce
import math
import sys
import heapq
from collections import deque
import time

start_time = time.time()

# O(N^2) ~ O(N)
# 거의 정렬된 상태면 빠름

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)


end_time = time.time()
print("time : ", end_time - start_time)
