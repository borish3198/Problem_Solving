# 조건을 만족하는 프로그램은 구성하였으나, 채점 시스템상 '시간초과' 문제 발생
# 시간 복잡도 분석 결과 최악의 경우 O(n^4)로 수정 필요
# 입력값 1000기준으로 최소 O(n^2)의 시간복잡도를 가지는 프로그램 작성 필요

from collections import deque
m, n = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

def bfs(i, j):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  queue = deque()
  queue.append((i,j))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if nx>=0 and nx<n and ny>=0 and ny<m:
        if graph[nx][ny]==0:
            graph[nx][ny] = graph[x][y]+1
            queue.append((nx,ny))
        elif graph[nx][ny]>=graph[x][y]+1:
            queue.append((nx,ny))
            graph[nx][ny]=graph[x][y]+1
        else:
            continue

for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
        bfs(i,j)

max=max(map(max, graph))

for i in range(n):
    if 0 in graph[i]:
        max=0

print(max-1)
