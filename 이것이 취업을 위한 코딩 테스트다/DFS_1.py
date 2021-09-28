# 음료수 얼려먹기
# 주어진 입력(0,1로 구성된 2차원 배열)에서 0으로 표현된 얼음 조각이 몇개나오는지 구하는 문제
# 얼음이 상하좌우로 연결돼 있을 경우 하나로 간주한다.
# DFS를 활용해 해결 가능

n, m = map(int, input().split())
ice = []
visited = []
for i in range(n):
    line = input()
    ice.append(list(line))
    visited.append([0]*m)

cnt = 0
def cream(x, y, ice, visited):
    if x>=0 and x<n and y>=0 and y<m: 
        if ice[x][y] == '0' and visited[x][y] == 0:
            visited[x][y] = 1
            cream(x-1, y, ice, visited)
            cream(x, y+1, ice, visited)
            cream(x-1, y, ice, visited)            
            cream(x, y-1, ice, visited)            
            return True

for j in range(n):
    for k in range(m):
        if cream(j,k,ice,visited) == 1:
            cnt+=1

for i in range(n):
    print(visited[i])

print(cnt)
