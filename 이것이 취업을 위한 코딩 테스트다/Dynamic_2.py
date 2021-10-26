'''
dynamic programming bottom-up variation
'''


n = int(input())
d = list(map(int, input().split()))
max = [0]*101

for i in range(1, n):
    if d[i]>d[i-1]:
        max[i+1] = max[i-1] + d[i]
    else:
        max[i+1] = max[i]

print(max[n])
