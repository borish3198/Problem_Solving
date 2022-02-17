t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    table = []
    for i in range(0, n*m, m):
        table.append(data[i:i+m])

    for j in range(1, m):
        for i in range(n):
            temp = table[i][j]
            table[i][j] = table[i][j-1]+temp

            if (i-1)>=0:
                table[i][j] = max(table[i][j], table[i-1][j-1] + temp)
            
            if (i+1)<n:
                table[i][j] = max(table[i][j], table[i+1][j-1] + temp)
    
    answer = 0
    for i in range(n):
        answer = max(answer, table[i][m-1])

    print(answer)
