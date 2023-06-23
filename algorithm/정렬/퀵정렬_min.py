from functools import reduce
import math
import sys
import heapq
from collections import deque
import time

start_time = time.time()

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소 갖고있으면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]  # 피봇 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽

    # 분할 이후 왼쪽 오른쪽 각가 정렬 수행 후 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))


end_time = time.time()
print("time : ", end_time - start_time)
