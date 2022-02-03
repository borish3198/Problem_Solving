'''
- 문제의 조건 중 시작도시의 거리는 0으로 지정하도록 함.
- 각 도시까지의 거리를 기록하는 dist배열을 0으로 초기화 하였고, 시작도시도 마찬가지로 0에서 변동 없도록 함.
- 그 결과 이웃노드를 갔다가 다시 시작도시로 가는 경우가 생기게 됨(조건이 not dist[i]이기 때문에)
- 해당 부분 dist 배열을 -1로 초기화하여 해결
'''


from collections import deque
import sys

input = sys.stdin.readline

def bfs(dist, v, graph):
    queue = deque([v])
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if dist[i]==-1:
                queue.append(i)
                dist[i]=dist[a]+1

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [-1]*(n+1)
dist[x] = 0

bfs(dist, x, graph)

cnt=0
for i in range(1, n+1):
    if dist[i]==k:
        print(i)
        cnt+=1

if cnt==0:
    print(-1)
