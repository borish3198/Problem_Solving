'''
add 함수에서 새로 추가된 친구가 이미 딕셔너리에 있는지 확인하고자 in 함수를 사용하였는데, 이 때 paret.keys()를 리스트로 변환하지 않고 그대로 사용, 시간초과 문제 해결
input, print 대신 sys라이브러리의 stdin, stdout 사용하여 실행시간 단축
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
        
    
    
