# DFS와 BFS
# 제공되는 데이터는 정점, 간선, 시작 번호와 정점 간의 연결 관계이다
# 이 데이터를 연결리스트 형태로 바꾼다
# 이후 DFS, BFS 함수를 구현해 경로를 출력하면 완성

from collections import deque

n, m, s = map(int, input().split())
graph = []
for i in range(n+1):
    graph.append([])

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

visited = []
def DFS(s, visited):
    print(s, end=" ")
    visited.append(s)
    for i in graph[s]:
        if i not in visited:
            DFS(i, visited)

def BFS(s):
    print()
    queue = deque()
    visited = []
    visited.append(s)
    queue.append(s)
    while queue:
        ns = queue.popleft()
        print(ns, end=" ")
        for i in graph[ns]:
            if i not in visited:
                queue.append(i)
                visited.append(i)

DFS(s, visited)
BFS(s)
