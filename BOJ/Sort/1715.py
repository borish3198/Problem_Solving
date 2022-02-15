'''
우선순위 힙 자료구조를 통해 해결할 수 있는 문제
우선순위 힘은 차치하더라도
최초 문제를 풀 당시 문제 해결을 위한 올바른 접근도 하지 못했다
'''

import heapq
import sys

input = sys.stdin.readline

n = int(input())

heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)
