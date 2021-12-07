'''
다익스트라 알고리즘에 대한 막연한 두려움이 있었는데 해소할 수 있는 기회였다.
간단하게 구현한 다익스트라 알고리즘으로는 시간 초과 문제로 해결할 수 없었는데,
최소 경로 문제의 경우 힙정렬을 활용한 우선수위 큐로 구현된 다익스트라 알고리즘을 기본으로 사용해야겠다.
'''


import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0 
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else: print(distance[i])
