"""
LIS 알고리즘으로 해결할 수 있는 문제
"""


n = int(input())
data = list(map(int, input().split()))

dp = [1]*(n)
dp[0] = 1

data.reverse()

for i in range(1, n):
    for j in range(0, i):
        if data[i]>data[j]: 
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))      
