'''
최소 신장트리 활용 문제
- 노드의 개수와 각 노드의 좌표만 주어짐
- 모든 노드 간의 간선 거리를 계산하여 노드 정보로 입력 : 시간 복잡도 O(n^2)
- 크루스칼 알고리즘 활용하여 문제 해결
- 입력 값이 100개에 한정되어 풀이 가능한 문제
- 제곱근 구하는 라이브러리 함수 math.sqrt()
'''


import math
import sys

input = sys.stdin.readline

def find(k):
    if k != parent[k]:
        parent[k] = find(parent[k])
    return parent[k]

def union(a, b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def distance(a, b):
    x, y = a
    z, w = b
    result = math.sqrt(pow((x-z),2) + pow((y-w),2))
    return round(result, 2)

n = int(input())
node = []
parent = [0]*(n)
edges = []
answer = 0

for i in range(n):
    a, b = map(float, input().split())
    node.append((a, b))
    parent[i] = i

for i in range(n-1):
    a = node[i]
    for j in range(i+1, n):
        b = node[j]
        c = distance(a, b)
        edges.append((c, i, j))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a,b)
        answer+=cost

print(answer)
