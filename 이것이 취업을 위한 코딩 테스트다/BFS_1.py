# 미로 최단 경로 찾기 문제

n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

def runner(i, j, maze):
    route = 0

    while i!=n and j!=m:
        if i>=0 and i<n and j>=0 and j<m:
            if maze[i][j]==0:
                
