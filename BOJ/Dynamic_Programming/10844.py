'''
오랜만에 스스로 해결한 문제
답을 10억으로 나누는 문제여서, 과거의 사례를 떠올리고 모든 값에 10억을 나눴으나 정작 n(입력값)이 최대일때 값이 10억이 넘어 조건을 만족하지 못했음.
이 경우 답에만 10억을 나눴을 때 문제가 없었으나, 문제 중에는 해당 조건이 나왔을 경우 값이 너무 커져 모든 값에 나머지 값을 적용해야 할 수도 있음.
'''


import sys
n = int(sys.stdin.readline())

data = [0,1,1,1,1,1,1,1,1,1]
ans = [0 for _ in range(10)]

for i in range(n-1):
    for j in range(10):
        if j==0:
            ans[j] = data[1]
        elif j==9:
            ans[j] = data[8]
        else:
            ans[j] = (data[j-1])+(data[j+1])
    data = ans.copy()

ans = sum(data)
print(ans%1000000000)
