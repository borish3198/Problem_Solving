"""
크루스칼 알고리즘을 활용하여 해결할 수 있는 MST문제
최초 문제풀이는 맞았으나, 소수점 2자리 표현에 불필요한 코드를 추가해 1주일 넘게 해맴

* 계속 틀린 이유 : 두 좌표의 거리를 계산하는 함수 'distacne' 결과 값에 round함수를 추가하여 최종값에 오차가 생김
"""


import math
import sys

input = sys.stdin.readline

def dist(a, b):
    x, y = a
    w, z = b
    distance = math.sqrt(pow((x-w), 2) + pow((y-z),2))
    return distance

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a<b:
        parent[b]=a
    else:
        parent[a] = b

n, m = map(int, input().split())

node = []
edges = []
parent = [0]*(n)
cost = 0

for i in range(n):
    x, y = map(int, input().split())
    node.append((x, y))
    parent[i] = i

for i in range(n-1):
    a = node[i]
    for j in range(i+1, n):
        b = node[j]
        c = dist(a, b)
        edges.append((c, i, j))

edges.sort()

for i in range(m):
    a, b = map(int, input().split())
    union(a-1, b-1)

for edge in edges:
    c, a, b = edge
    if find(a)!=find(b):
        union(a, b)
        cost+=c
    
print("%.2f"%cost)
