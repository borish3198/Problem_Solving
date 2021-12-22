'''
1트 : 시간초과 발생  ->  union, find 함수에 리스트 포함 X
2트 : 시간초과 발생  ->  input, print 대신 sys.stdin.readline / sys.stdout.write 사용
3트 : recursion error 발생  ->  sys.setrecursionlimit() 사용

* 중요한 사례가 되는 문제
'''


import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def check_parent(a):
    if a != parent[a]:
        parent[a] = check_parent(parent[a])
    return parent[a]

def union(a, b):
    x = check_parent(a)
    y = check_parent(b)
    if x<y:
        parent[y] = x
    else:
        parent[x] = y

def check(a, b):
    x = check_parent(a)
    y = check_parent(b)
    if x==y:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")

n, m = map(int, input().split())

parent = [0]*(n+1)

for i in range(n+1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    if a==0:
        union(b, c)
    else:
        check(b, c)
        
