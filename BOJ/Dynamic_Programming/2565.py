import sys

input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

data.sort()

a = [1]*(n)
for i in range(n):
    temp = 0
    for j in range(i):
        if data[i][0]>data[j][0] and data[i][1]>data[j][1]:
            temp = max(temp, a[j])
    a[i] = temp+1

print(n-max(a))
