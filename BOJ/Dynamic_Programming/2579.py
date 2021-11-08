n = int(input())
stair = [0]
stair += [int(input()) for _ in range(n)]
data = [0]*(n+1)
data_2 = [0]*(n+1)

data[1] = stair[1]
flag = 1
for i in range(2, n+1):
    next = data[i-1] + stair[i]
    next_2 = data[i-2] + stair[i]

    if next>next_2 and flag<2:
        data[i] = next
        flag+=1
    else:
        data[i] = next_2
        flag=1

data_2[2] = stair[2]
flag=1
for i in range(3, n+1):
    next = data_2[i-1] + stair[i]
    next_2 = data_2[i-2] + stair[i]

    if next>next_2 and flag<2:
        data_2[i] = next
        flag+=1
    else:
        data_2[i] = next_2
        flag=1

print(max(data[n], data_2[n]))
