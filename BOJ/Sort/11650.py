# 계수정렬을 변형하여 문제 풀이

import sys

n = int(input())
data = [0]*200001

for i in range(n):
    a, b = map(int, input().split())
    point = a+100000
    if data[point]:
        new = data[point]
        new.append(b)
        data[point] = new
    else:
        data[point] = [b]

for i in range(200001):
    if data[i]!=0:
        new = data[i] 
        new.sort()
        for j in new:
            print(i-100000, j)
