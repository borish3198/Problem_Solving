# 2차원 토마토 문제를 3차원으로 바꾼 문제
# 이에 따라 주어지는 데이터 값도 바뀌고, 주변에 익힐 수 있는 토마토의 수도 늘어남(위, 아래 추가)
# 최초 3차원 배열로 문제 해결하였으나 시간 초과 문제 발생
# 2차원 배열을 활용한 3차원 배열 구현으로 문제 해결
# 3차원 데이터가 주어졌을 때 무조건 3차원 배열을 구현하는 것이 아니라
# 2차원으로 해결하는 것이 효율적일 때가 있다는 사실을 배움
# 생각할 거리 : 그렇다면 언제 3차원 구현하고, 언제 2차원 구현할까?
# 생각할 거리 : 배열 상 2차원, 3차원에서 데이터를 불러오는데 시간차이가 그렇게 많이 날까?

from collections import deque
m, n, o = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n*o)]

def bfs(): 
  dx = [-1, 1, 0, 0, n, -n]
  dy = [0, 0, -1, 1, 0, 0]
  while queue:
    x, y = queue.popleft()
    old = graph[x][y]
    for i in range(4):
      nx = x+dx[i]
      s = x//n
      ny = y+dy[i]
      if nx>=n*s and nx<n*(s+1) and ny>=0 and ny<m:
        next = graph[nx][ny]
        if next==0:
            graph[nx][ny] = old+1
            queue.append((nx,ny))
    for i in range(4,6):
      nx = x+dx[i]
      ny = y+dy[i]
      if nx>=0 and nx<n*o and ny>=0 and ny<m:
        next = graph[nx][ny]
        if next==0:
            graph[nx][ny] = old+1
            queue.append((nx,ny))

    
  flag = 0
  max = 0
  for i in range(n*o):
    for j in range(m):
      if graph[i][j]==0:
        return -1
      if graph[i][j]>=max:
          max=graph[i][j]
  return max-1

queue = deque()
for i in range(n*o):
  for j in range(m):
    if graph[i][j]==1:
        queue.append((i,j))

print(bfs())
