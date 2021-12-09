'''
1504문제 2트
플로이드 워셜 알고리즘 들고 문제 풀이 시도했으나 시간 초과
노드의 개수가 100개가 넘어갈 경우 시간복잡도가 O(N^3)인 플로이드 워셜 알고리즘은 사용 불가능하다.
'''


import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

v1, v2 = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[b][k])

a1 = graph[1][v1] + graph[v1][v2] + graph[v2][n]
a2 = graph[1][v2] + graph[v2][v1] + graph[v1][n]

answer = min(a1, a2)

if answer>=INF:
    print(-1)
else:
    print(answer)
