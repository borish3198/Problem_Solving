import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(parent, k):
    if k != parent[k]:
        parent[k] = find(parent, parent[k])
    return parent[k]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

t = int(input())

for i in range(t):
    n,m = map(int, input().split())
    parent = [0]*(n+1)
    plane = []
    cnt = 0

    for i in range(n+1):
        parent[i] = i

    for _ in range(m):
        a, b = map(int, input().split())
        plane.append((a,b))

    for jet in plane:
        a, b = jet
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            cnt +=1
    
    print(cnt)

