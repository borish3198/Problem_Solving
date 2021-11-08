n = int(input())
pyramid = []
for i in range(n):
    pyramid.append(list(map(int, input().split())))

data = [[0 for _ in range(n)] for _ in range(n)]


data[0][0] = pyramid[0][0]

for i in range(0, n-1):
    for j in range(0, i+1):
        next = data[i][j] + pyramid[i+1][j]
        if next>data[i+1][j]:
            data[i+1][j] = next
        next = data[i][j] + pyramid[i+1][j+1]
        if next>data[i+1][j+1]:
            data[i+1][j+1] = next
        
print(max(data[n-1]))
