# The problem requires number of groups that consist of '1'  * connection only count when number '1' is connected in 4 ways(up, down, left, right)
# also requires number of '1' in each group
# It was challenging for me to implement counting how many times the recursive funtion has been operated.
# Using global variant, it could be solved. but I believe there must be better and more effective way to solve it.

n = int(input())
graph=[]
for i in range(n):
  graph.append(list(map(int, input())))

def dfs(i, j):
  global q
  if graph[i][j]==0: 
    return 0
  else:
    graph[i][j]=0
    q+=1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for h in range(4):
      ni = i + dx[h]
      nj = j + dy[h]
      if ni>=0 and ni<n and nj>=0 and nj<n:
        dfs(ni, nj)
    return True

cnt = 0
group = []
for x in range(n):
  for y in range(n):
    q=0
    ans = dfs(x, y)
    if ans:
      cnt+=1
      group.append(q)

group.sort()
print(cnt)
for i in group:
  print(i)
