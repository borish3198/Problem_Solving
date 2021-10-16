# 기본기가 중요한 이유 : 간단하게 해결할 수 있는 코드를 복잡하고 길게 작성하게 된다.
# 다중 조건 정렬의 경우 lambda를 이용해 간단하게 해결 가능
# sort함수의 키 값으로 람다함수를 선언하여 첫번째, 두번째 원소를 조건으로 줄 경우 간단하게 문제 해결 가능
# 만약 내림차순 정렬이 필요한 경우 lambda x:(x[0], -x[1]) 이런식으로 내림차순 정렬이 필요한 곳에 '-' 붙이면 된다.


import sys
n = int(input())
data=[]
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
data.sort(key=lambda x:(x[0], x[1]))
for j in data:
    print(j[0], j[1])
