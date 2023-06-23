from functools import reduce
import math
import sys
import heapq
from collections import deque
import time

start_time = time.time()

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개이면 종료
        return
    pivot = start  # 첫번째 원소 피봇
    left = start + 1
    right = end
    while left <= right:
        # 피봇보다 큰 데이터 찾을때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피봇보다 작은 데이터 찾을때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 엇갈렸다면 작은 데이터와 피봇 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right],
        # 엇갈리지 않았다면 작은데이터와 큰 데이터 교체
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행(피봇 좌우 묶음에서)
    quick_sort(array, start, right - 1)  # 왼쪽
    quick_sort(array, right + 1, end)  # 오른쪽


quick_sort(array, 0, len(array) - 1)
print(array)


end_time = time.time()
print("time : ", end_time - start_time)
