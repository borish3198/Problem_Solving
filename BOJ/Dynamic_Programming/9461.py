n = int(input())
target = [int(input()) for _ in range(n)]
len = max(target)+1
if len<6:
    len = 10
d = [0]*(len)

d[1]=d[2]=d[3]=1
d[4]=d[5]=2
for i in range(6, max(target)+1):
    d[i] = d[i-1]+d[i-5]

for i in target:
    print(d[i])
