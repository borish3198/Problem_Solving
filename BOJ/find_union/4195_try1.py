'''
시간 초과로 실패
'''

n = int(input())

def find(a):
    if a!=parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def add(a):
    if a not in list(parent.keys()):
        parent[a] = a
        count[a] = 1

def union(a, b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b]=a
        count[a]+=count[b]
    else:
        parent[a]=b
        count[b]+=count[a]

for i in range(n):
    m = int(input())
    parent = {}
    count = {}
    for _ in range(m):
        a, b = map(str, input().split())
        add(a)
        add(b)
        union(a, b)
        if a<b:
            print(count[find(a)])
        else:
            print(count[find(b)])
        
    
    
