import sys

INF = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        print(graph[a][b], end=" ")
    print()
