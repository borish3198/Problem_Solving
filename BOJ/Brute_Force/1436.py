# 666이 들어간 n번째 숫자를 찾는 프로그램
# 시간복잡도 O(n)의 간단한 문제

n = int(input())
name = 0

while True:
    name+=1
    if '666' in str(name):
        n-=1
    if n==0:
        print(name)
        break
