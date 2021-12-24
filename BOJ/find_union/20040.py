'''
1트 : 사이클이 완성된 이후 입력 값의 내용에 따라 answer값이 변경되는 구조로 오답
2트 : 해당부분 수정하여 문제 해결
'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b] = a
    elif b<a:
        parent[a] = b

parent = [0]*(n)
for i in range(n):
    parent[i] = i

cycle = False

for k in range(m):
    a, b = map(int, input().split())
#문제 해결한 부분 *****************************************************
    if cycle:
        continue
    if find(a) == find(b):
        cycle = True
        answer = k+1
    else:
        union(a, b)

if cycle==False:
    print(0)
else:
    print(answer)
