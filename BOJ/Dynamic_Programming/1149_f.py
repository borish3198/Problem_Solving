'''
나중에 꺼내보고 반성하라는 의미의 기록
백준 dP문제 1149를 풀며 잘못 접근했을 때의 코드
'''

n = int(input())
rgb = [[0,0,0]]
d = [0]*(n+1)
idx = [0]*(n+1)

for i in range(n):
    rgb.append(list(map(int, input().split())))
d[1] = min(rgb[1])
idx[0] = 4
idx[1] = rgb[1].index(d[1])
rgb[1][idx[1]] = 1001

for i in range(2, n+1):
    min_v = min(rgb[i]) 
    min_idx = rgb[i].index(min_v)
    rgb[i][min_idx] = 1001
    if idx[i-1] == min_idx:
        alpha = min(rgb[i-1])+min_v+d[i-2]
        temp = rgb[i-1].index(min(rgb[i-1]))
        if idx[i-2] == rgb[i-1].index(min(rgb[i-1])):
            temp_idx = [0, 1, 2]
            temp_idx.remove(rgb[i-1].index(min(rgb[i-1])))
            temp_idx.remove(rgb[i-1].index(max(rgb[i-1])))
            temp = temp_idx[0]
            alpha = rgb[i-1][temp_idx[0]]+min_v+d[i-2]    
        d[i] = min(d[i-1] + min(rgb[i]), alpha)
        if d[i]==d[i-1] + min(rgb[i]):
            min_idx = rgb[i].index(min(rgb[i]))
        else:
            idx[i-1]=temp
        idx[i] = min_idx
    else:
        d[i] = min_v + d[i-1]
        idx[i] = min_idx
    rgb[i][min_idx]=1001
print(d[n])

print(d)
print(idx)
