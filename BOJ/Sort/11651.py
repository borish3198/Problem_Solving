# 11650.py 문제에서 정렬기준이 변경된 문제
# 마찬가지로 sort()함수의 다중 조건을 활용해 문제 해결 가능

import sys
n = int(input())
data=[]
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
data.sort(key=lambda x:(x[1], x[0]))
for j in data:
    print(j[0], j[1])
