'''
파라메트릭 서치 유형의 문제 = '원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제'
최적화 문제의 경우 이진탐색을 통해 해결 가능
* 탐색 범위가 1부터 10억까지의 정수, 큰 수의 탐색 범위가 있을 경우 이진 탐색을 떠올리기
'''

import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(data)

while start<=end:
    mid = (start+end)//2
    sum=0
    for i in range(n):
        rc = data[i]-mid
        if rc>0:
            sum+=rc
    if sum<m:
        end = mid-1
    else:
        result = mid
        start = mid+1        

print(result)
