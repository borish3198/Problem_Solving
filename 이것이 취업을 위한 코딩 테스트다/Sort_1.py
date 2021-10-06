# 선택 정렬을 활용한 내림차순 구현

data = [int(input()) for _ in range(int(input()))]

def sort(data):
    for i in range(len(data)):
        max=i
        for j in range(i+1, len(data)):
            if data[max]<data[j]:
                max=j
        data[i], data[max] = data[max], data[i] 
    return(data)

for i in sort(data):
    print(i, end=" ")
