import sys

input = sys.stdin.readline

def find(a):
    if a!= parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
m = int(input())

parent = [0]*(n+1)
for i in range(n):
    parent[i] = i

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))
plan = list(map(int, input().split()))


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i+1,j+1)

old = find(plan[0])
for i in plan:
    if old == find(i):
        continue
    else:
        old=-1
        print("NO")
        break
        
if old>=0:
    print("YES")
