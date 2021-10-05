# 이틀 동안 고민한 토마토 문제, 문제는 큐의 동작 원리를 망각한데 있다.
# BFS의 경우 큐를 사용하는데, DFS처럼 재귀적으로 동작하는 것으로 착각하여
# 불필요한 조건을 추가하였고, 결과적으로 불필요한 경로를 탐색하여 시간초과가 발생했다.
# 문제가 이상하게 복잡해지거나 안풀리는 경우 내가 알고 있는 것이 과연 맞는지 되돌이켜 생각해보는 습관을 갖자.

from collections import deque
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs():
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  while queue:
    x, y = queue.popleft()
    old = graph[x][y]
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if nx>=0 and nx<n and ny>=0 and ny<m:
        next = graph[nx][ny]
        if next==0:
            graph[nx][ny] = old+1
            queue.append((nx,ny))
    
  flag = 0
  max = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j]==0:
        return -1
      if graph[i][j]>=max:
          max=graph[i][j]
  return max-1

queue = deque()
for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
        queue.append((i,j))

print(bfs())
