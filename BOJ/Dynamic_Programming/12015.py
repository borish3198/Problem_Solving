import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
dp = []

dp.append(data[0])

for i in range(1, n):
    if data[i]>dp[-1]:
        dp.append(data[i])
    else:
        idx = bisect_left(dp, data[i])
        dp[idx] = data[i]
 
print(len(dp))

