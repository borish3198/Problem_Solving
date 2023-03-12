import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
# 그래프, 최소 거리 테이블, 방문 여부 확인 자료형
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)
# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
# 최소 거리 노드 확인 함수
def find_min():
    min = INF
    idx = 0
    for i in range(1, n+1):
        if distance[i] < min and not visited[i]:
            min = distance[i]
            idx = i
    return idx

def dijkstra(start):
    # 시작 노드 초기화
    visited[start] = True
    distance[start] = 0
    # 최소 거리 테이블 초기화
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 다른 노드에 대해 반복
    for _ in range(2, n+1):
        now = find_min()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    print(distance[i])
