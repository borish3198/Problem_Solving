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

이틀째 문제 풀이 중
'''
