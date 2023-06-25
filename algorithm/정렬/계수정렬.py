from functools import reduce
import math
import sys
import heapq
from collections import deque
import time

start_time = time.time()

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

end_time = time.time()
print("time : ", end_time - start_time)
