'''
결국 스스로 생각하지는 못한 문제
다익스트라 알고리즘으로 특정 지점에서 다른 곳까지의 거리만 출력하도록 변형하여
다익스트라 알고리즘 수행을 최소화

의문점 : gh 사이 거리를 다익스트라로 해야 하는 이유?
정답 : 문제에선 gh사이를 무조건 지나도록 조건을 제시했지만, 다익스트라로 풀 경우 gh사이의 최단 거리를 계산해
       실제 gh 사이의 거리값이 아닌 다른 값이 들어갈 수 있음.
'''


import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline
answer = []

T = int(input())

def dijkstra(start):
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
    return distance

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
        if (a==g and b==h) or (a==h and b==g):
            gh_dist = c

    for _ in range(t):
        target.append(int(input()))

    ans = []
    s_distance = dijkstra(s)
    g_distance = dijkstra(g)
    h_distacne = dijkstra(h)

    for t in target:
        can = min(s_distance[g] + h_distacne[t], s_distance[h] + g_distance[t])
        if s_distance[t] == (can + gh_dist) and can<INF:
            ans.append(t)

    answer.append(sorted(ans))

for ans in answer:
    for i in ans:
        print(i, end=" ")
    print()

