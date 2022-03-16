n, k = map(int, input().split())
coins = []
ans = 0

for i in range(n):
    coins.append(int(input()))

for i in range(n-1, -1, -1):
    if k==0:
        break
    coin = coins[i]
    num = k//coin
    if num != 0:
        ans += num
        k -= (num*coin)

print(ans)
