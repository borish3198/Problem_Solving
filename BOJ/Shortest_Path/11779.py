import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

INF = n*100000 + 1

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])

start, end = map(int, input().split())

path = [[start] for i in range(n+1)]
distance = [INF]*(n+1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        temp = INF
        for j in range(len(graph[now])):
            i = graph[now][j]
            cost = dist + i[1]
            if distance[i[0]]>cost:
                distance[i[0]] = cost   
                path[i[0]] = path[now] + [i[0]]

                heapq.heappush(q, (cost, i[0]))
            
dijkstra(start)
print(distance[end])
print(len(path[end]))
for i in path[end]:
    print(i, end=' ')
