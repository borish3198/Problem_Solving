'''
2트 : 문제의 접근은 맞으나 다익스트라 알고리즘 호출 횟수가 너무 많아 33%에서 시간 초과
'''

import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline
answer = []

T = int(input())

def dijkstra(start, end):
    q = []
    distance = [INF] * (n+1)
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
                heapq.heappush(q, (cost, j[0]))
    return distance[end]

# def check(s, g, h, t):
#     val1 = dijkstra(s, g) + dijkstra(g, h) + dijkstra(h, t)
#     val2 = dijkstra(s, h) + dijkstra(h, g) + dijkstra(g, t)
#     return min(val1, val2)

for i in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    target = []

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b,c)) 
        graph[b].append((a,c))

    for _ in range(t):
        target.append(int(input()))

    ans = []
    
    g_distance = dijkstra(s, g)
    h_distance = dijkstra(s, h)
    gh_distacne = dijkstra(g, h)

    for t in target:
        can = min(g_distance + gh_distacne + dijkstra(h, t), h_distance + gh_distacne + dijkstra(g, t))
        if dijkstra(s, t) == can and can<INF:
            ans.append(t)

    answer.append(sorted(ans))

for ans in answer:
    for i in ans:
        print(i, end=" ")
    print()
