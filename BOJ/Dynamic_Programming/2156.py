'''

'''

import sys

n = int(sys.stdin.readline())
d = [int(sys.stdin.readline()) for _ in range(n)]
a = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        a[i] = d[i]
    elif i==1 :
        a[i] = d[i] + d[i-1]
    elif i==2 :
        a[i] = max(d[0]+d[1], d[1]+d[2], d[0]+d[2])
    else:
        a[i] = max(a[i-3]+d[i-1]+d[i], a[i-2]+d[i], a[i-1])

print(a[n-1])
