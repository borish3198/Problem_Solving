import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline
answer = []

T = int(input())

def dijkstra(start, end, graph):
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

def check(s, g, h, t, graph):
    val1 = dijkstra(s, g, graph) + dijkstra(g, h, graph) + dijkstra(h, t, graph)
    val2 = dijkstra(s, h, graph) + dijkstra(h, g, graph) + dijkstra(g, t, graph)
    return min(val1, val2)

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
    for t in target:
        can = check(s, g, h, t, graph)
        if dijkstra(s, t, graph) == can and can<INF:
            ans.append(t)

    answer.append(sorted(ans))


for ans in answer:
    for i in ans:
        print(i, end=" ")
    print()
