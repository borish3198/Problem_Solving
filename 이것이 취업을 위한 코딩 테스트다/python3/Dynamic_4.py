import sys
n, m = map(int, input().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]
coin.sort(reverse=True)
d = [0]*101
for i in range(min(coin)):
    d[i]=-1
for i in range(min(coin), m+1):
    k=[]
    for j in coin:
        if i-j==0:
            k.append(1)
        if i>j:
            if d[i-j]+1>0:
                k.append(d[i-j]+1)
    if len(k)==0:
        d[i]=-1
    else:
        d[i] = min(k)
print(d)
