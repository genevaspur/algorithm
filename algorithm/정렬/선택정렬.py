from functools import reduce
import math
import sys
import heapq
from collections import deque
import time

start_time = time.time()

# O(N^2)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]


print(array)


end_time = time.time()
print("time : ", end_time - start_time)
