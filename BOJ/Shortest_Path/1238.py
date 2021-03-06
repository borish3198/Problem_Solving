import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
time = [0]*(n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start, end):
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]]>cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[end]

for i in range(1, n+1):
    time[i] = dijkstra(i, x) + dijkstra(x, i)

print(max(time))
