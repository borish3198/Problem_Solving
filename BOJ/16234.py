"""
pypy3 solved / python 3 : time over
"""


from collections import deque

def bfs(i, j):
    queue = deque([(i, j)])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    temp[i][j] = 1
    sum = 0
    group = [(i, j)]

    while queue:
        x, y = queue.popleft()
        sum += data[x][y]
        conA = data[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx>=0 and nx<n and ny>=0 and ny<n and temp[nx][ny]==0:
                conB = data[nx][ny]
                diff = abs(conA-conB)
                if diff>=l and diff<=r:
                    queue.append((nx, ny))
                    group.append((nx, ny))
                    temp[nx][ny] = 1

    new_pop = sum//len(group)
    # print(i, j, group)
    for x, y in group:
        data[x][y] = new_pop

    # for i in range(n):
    #     for j in range(n):
    #         print(data[i][j], end = " ")
    #     print()

    # print("*******************************")
    if len(group) == 1:
        return False
    else:
        return True

n, l, r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*(n) for _ in range(n)]
day = 0
flag = 0

while True:
    count = 0
    day+=1
    temp = [[0]*(n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if temp[i][j]==0:
                bfs(i, j)
                count+=1
    if count == n*n:
        break

print(day-1)
