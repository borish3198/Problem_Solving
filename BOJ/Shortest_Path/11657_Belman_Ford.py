import sys

input = sys.stdin.readline
INF = int(1e9)
n, v = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(v)]

def belman(start):
    dist = [INF]*(n+1)
    dist[start] = 0

    for _ in range(n-1):
        for a, b, w in graph:
            if dist[a] != INF and dist[a] + w < dist[b]:
                dist[b] = dist[a] + w

    cycle = 0
    for a, b, w in graph:
        if dist[a] != INF and dist[a] + w < dist[b]:
            cycle = 1

    if cycle:
        return -1

    else:
        return dist

ans = belman(1)
if ans==-1:
    print(-1)
else:
    for i in range(2, n+1):
        if ans[i] == INF:
            print(-1)
        else:
            print(ans[i])


    
