import sys

input = sys.stdin.readline

def find(k):
    if k!=parent[k]:
        parent[k] = find(parent[k])
    return parent[k]

def union(a, b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
    
v, e = map(int, input().split())

parent = [0]*(v+1)
graph = []
cost = 0

for i in range(v):
    parent[i] = i

for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

for edge in graph:
    c, a, b = edge
    if find(a) != find(b):
        union(a, b)
        cost+=c

print(cost)


