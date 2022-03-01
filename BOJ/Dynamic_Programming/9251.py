a = input()
b = input()

n = len(a)
k = len(b)

data = list([0]*(k+1) for _ in range(n+1))

val = 0

for i in range(1, n+1):
    for j in range(1, k+1):
        if a[i-1] == b[j-1]:
            data[i][j] = data[i-1][j-1] + 1
        else:
            data[i][j] = max(data[i-1][j], data[i][j-1])
        val = max(val, data[i][j])

print(val)
