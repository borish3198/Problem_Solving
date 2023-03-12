# 미로 최단 경로 찾기 문제
# BFS 활용하여 문제 해결
# DFS/BFS를 문제에 어떻게 녹여낼지 고민하는 능력이 필요
# 이 문제에선 최단 경로를 어떻게 찾을지를 고민하는 것이 아니라 
# 모든 칸에 대해 시작점에서 몇 칸을 거쳐가는지를 미로에 기록하도록 함수를 짠 뒤
# 미로 출구의 값을 출력하면 문제를 해결할 수 있음.


from collections import deque

n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

def runner(i, j):
    queue = deque()
    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]
    queue.append((i,j))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    
    return(maze[n-1][m-1])

print(runner(0,0))






