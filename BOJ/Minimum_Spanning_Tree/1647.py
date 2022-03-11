import sys

input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
graph = []
parent = [i for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

last = 0
ans = 0
for edge in graph:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        last = cost
        ans += cost

print(ans-last)
