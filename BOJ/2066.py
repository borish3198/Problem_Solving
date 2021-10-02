# This problem requires the numver of computers infected considering the networks environment.
# The virus only can affect other computers that are connected in the network containing the host(#1)
# At the first line the number of computers are given and at the second line the number of connections are given
# In sequence, information of connections are offered

from collections import deque

n = int(input())
m = int(input())
graph = []
for i in range(n+1):
    graph.append([])

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

def BFS(s):
    ans=-1
    queue = deque()
    visited = []
    visited.append(s)
    queue.append(s)
    while queue:
        ns = queue.popleft()
        ans+=1
        for i in graph[ns]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
    return ans

Answer = BFS(1)
print(Answer)
