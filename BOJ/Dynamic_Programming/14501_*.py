n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
d = [0]*(n+1)

for i in range(1, n+1):
    t, p = data[i-1]
    if t+i-1>n:
        continue
    previous = d[i-1]
    if previous == 0:
        k = i-1
        while k>=0:
            k-=1
            if d[k] != 0:
                previous = d[k]
                break
    d[t+i-1] = max(previous + p, d[t+i-1])

print(max(d))


'''
반례
7
2 10
5 1
5 1
5 1
5 1
5 1
1 10
결국 문제풀이 실패, 교재 참고하여 문제 해결하였으나 아직까지 어떻게 이런 문제에 접근해야하는지 감이 안온다.
'''


n = int(input())

t = []
p = []
dp = [0]*(n+1)
max_value = 0

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(n-1, -1, -1):
    time = i + t[i]
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)

