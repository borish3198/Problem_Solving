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
        elif graph[nx][ny]==-1 or 1:
            continue
        else:
            queue.append((nx,ny))
            if graph[nx][ny]>=graph[x][y]+1:
                graph[nx][ny]=graph[x][y]+1

for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
        print(i,j)
        bfs(i,j)

for i in range(n):
    print(graph[i])

max=max(map(max, graph))
print(max-1)
