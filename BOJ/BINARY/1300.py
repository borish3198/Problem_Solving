n = int(input())
k = int(input())

start = 1
end = k

while start<=end:
    mid = (start + end)//2
    sum = 0
    for i in range(1, n+1):
        sum+=min(n, mid//i)       #특정 수 이하에 몇개의 숫자가 있는지 확인하는 이 개념을 떠올릴 수가 없었음.
    if sum>=k:                    #이분탐색 중 mid==target이 아닌 경우의 이분탐색에 대한 내용은 없었음. uppderbound, lowerbound 개념에 대한 공부 필요
        end = mid-1
    else:
        start = mid+1
    
print(start)
