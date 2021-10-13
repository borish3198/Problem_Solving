# 통계에서 필요한 여러 값들을 계산하는 문제
# 계수정렬을 이요해 구현하였으나, 요구하는 값들을 구현하는데 여러가지 어려움 있었음
# 특히 중간값, 최빈값(중복될 경우 두번째로 작은 값 요구) 구현 시 실수가 많음
# 지속적으로 문제 해설을 참고하는 습관 별로..



import sys

n = int(sys.stdin.readline())
data = [0]*8001
sum = 0

# 계수정렬
for i in range(n):
    k = int(sys.stdin.readline())
    data[k+4000]+=1
    sum+=k

# 중간값 구하기
mid_sum = (n+1)/2
mid = 0
old=0
for i in range(8001):
    if data[i]:
        mid_sum-=data[i]
        if mid_sum<=0:
            mid=i-4000
            break
    

# 최빈값 구하기
i=-1
j=0
freq_max = max(data)
if data.count(freq_max)>=2:
    while j!=2:
        i+=1
        if data[i]==freq_max:
            j+=1
    ans = i-4000
else:
    for i in range(8001):
        if data[i]==freq_max:
            ans=i-4000
            break

average = round(sum/n)

# 범위 구하기
s=-1
e=8001
while True:
    s+=1
    if data[s]:
        break
while True:
    e-=1
    if data[e]:
        break
diff = e-s

print(average)
print(mid)
print(ans)
print(diff)
