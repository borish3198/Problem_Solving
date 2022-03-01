n = int(input())
data = list(map(int, input().split()))

a = [1]*(n)
b = [1]*(n)

def dp(data, memory):
    for i in range(n):
        temp = 0
        for j in range(i):
            if data[j]<data[i]:
                temp = max(temp, memory[j])
        memory[i] = temp+1

dp(data, a)

data.reverse()

dp(data, b)

b.reverse()

ans=0
for i in range(n):
    ans = max(ans, a[i]+b[i])

print(ans-1)
