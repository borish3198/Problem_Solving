'''
input, print 대신 sys라이브러리의 stdin, stdout 사용하여 시간초과 문제 해결
but, 출력초과 문제 발생
'''

import sys
input = sys.stdin.readline

n = int(input())

def find(a):
    if a!=parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def add(a):
    if a not in parent.keys():
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
        if a==b:
            add(a)
            sys.stdout.write(str(count[find(a)])+'\n')
            continue
        add(a)
        add(b)
        union(a, b)
        if a<b:
            sys.stdout.write(str(count[find(a)])+'\n')
        else:
            sys.stdout.write(str(count[find(b)])+'\n')
        
    
    
