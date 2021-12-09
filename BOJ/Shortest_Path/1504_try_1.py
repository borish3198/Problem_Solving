'''
N개의 노드와 M개의 간선으로 구성된 무방향 그래프가 주어질 때 
노드 1에서 출발해 v1과 v2를 거쳐 N노드에 도달하는 최소거리를 구하는 문제

1트 : 1->v1->v2->N / 1->v2->v1->N 두 가지 경우가 있다고 판단하여
각각의 구간을 다익스트라 알고리즘으로 계산 후 그 값을 합하여
두 가지 경우에서 나온 값 중 더 작은 값을 가지는 값을 답으로 내었으나 
7%까지 문제 풀다가 실패!!
'''


import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q,(cost, j[0]))

    answer = distance[end]
    if answer==0:
        answer = INF
    return answer

a1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
a2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)


answer = min(a1, a2)

if answer>=INF:
    print(-1)
else:
    print(answer)
