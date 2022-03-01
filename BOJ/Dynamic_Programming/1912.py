n = int(input())
data = list(map(int, input().split()))
a = data.copy()

for i in range(1, n):
    a[i] =  max(data[i], a[i-1] + data[i])

print(max(a))
