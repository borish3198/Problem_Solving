import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = []
for i in range(n):
    data.append(tuple(map(int, input().split())))

a = [[0]*(k+1) for _ in range(n+1)]

data.sort()
ans = 0
for i in range(1, n+1):
    w, v = data[i-1]
    for j in range(1, k+1):
        if w<=j:
            a[i][j] = max(a[i-1][j], a[i-1][j-w] + v)
        else:
            a[i][j] = a[i-1][j]
        ans = max(ans, a[i][j])

print(ans)
