import sys

n = int(sys.stdin.readline())
data = []

for i in range(n):
    info = list(map(str, sys.stdin.readline().split()))
    info.append(i)
    data.append(info)

data.sort(key=lambda x:(int(x[0]), x[2]))
for i in data:
    print(i[0], i[1])
