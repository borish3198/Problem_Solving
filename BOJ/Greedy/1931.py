import sys

input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(tuple(map(int, input().split())))

data.sort()
ans = 1
start, end = data[0]

for i in range(1, n):
    ms, me = data[i]
    if me<end:
        end = me
    elif ms>=end:
        end = me
        ans+=1
    
print(ans)
        
