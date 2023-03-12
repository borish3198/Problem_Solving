from itertools import combinations
import copy

def dfs(graph, i, j):
    graph[i][j] = 4
    move = [[-1, 0], [0, +1], [+1, 0], [0, -1]]
    for a, b in move:
        x = i+a
        y = j+b
        if x<0 or x>=n or y<0 or y>=m:
            continue
        if graph[x][y] == 0:
            dfs(graph, x, y)

def count_z(graph):
    cnt=0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt+=1
    return cnt

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
empty = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i, j))

wall = list(combinations(empty, 3))
ans = 0

for w in wall:
    temp = copy.deepcopy(graph)
    for loc in w:
        temp[loc[0]][loc[1]] = 1
    for i in range(n):
        for j in range(m):
            if temp[i][j]==2:
                dfs(temp, i, j)
    ans = max(ans, count_z(temp))

print(ans)
