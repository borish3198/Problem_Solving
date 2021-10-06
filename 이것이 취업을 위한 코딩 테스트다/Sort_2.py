# 삽입정렬을 활용한 오름차순

data = [list(map(str, input().split())) for _ in range(int(input()))]
def point(i):
    return int(data[i][1])
    
for i in range(1, len(data)):
    for j in range(i, 0, -1):
        if point(j)<point(j-1):
            data[j], data[j-1] = data[j-1], data[j]

for i in data:
  print(i[0], end=" ")
