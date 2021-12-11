'''
1504 3트만에 성공
1트 때 아이디어는 그대로 사용하되 1트 코드의 문제점 확인
* 코드 초반 전역변수로 선언한 distace 리스트가 문제의 시발점
  해당 테이블을 초기화하지 않은 채 다익스트라 알고리즘을 반복하면서 기존 남아있던 데이터가 알고리즘 수행에 영향을 미침 
  distance 리스트 선언을 함수 내부에서 실행하여 함수 실행 때마다 최신화하여 문제 해결함.
'''
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    distance = [INF]*(n+1)              #*************************************문제의 포인트*****************************************************************
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q,(cost, j[0]))

    answer = distance[end]
    return answer

a1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
a2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

answer = min(a1, a2)

if answer>=INF:
    print(-1)
else:
    print(answer)
