import sys

input = sys.stdin.readline

n, c = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()

start = 1
end = data[-1] - data[0]
ans = 0

while True:
    if start>end:
        break
    count = 1
    prev = data[0]
    mid = (start+end)//2
    for i in range(1, n):
        if data[i] >= prev + mid:
            count+=1
            prev = data[i]

    
    if count>=c:
        ans = mid
        start = mid+1
    else:
        end = mid-1

print(ans)
