# 몇개월 간 고심하게 한 별찍기 문제
# 해당 코드로 답은 나오지만 채점 시 '시간 초과' 오류가 뜸.
# 조건문이 연달아 있는 구조여서 생기는 문제 같은데 정확한 원인을 파악하지 못함.
# 복잡도 분석을 통해 문제의 원인 확인할 예정!
# 다른 사람이 푼 모범답안도 같이 첨부함.

import sys

def star(n,i,j):
    if n==3:
        if i%3==1 and j%3==1:
            sys.stdout.write(" ")
        else:
            sys.stdout.write("*")
    else:
        if i%n>=(n/3) and i%n<(n/3)*2 and j%n>=(n/3) and j%n<(n/3)*2:
            sys.stdout.write(" ")
        else:
            star(n/3, i, j)

n=int(input())

for i in range(n):
    for j in range(n):
        star(n, i, j)
    sys.stdout.write('\n')
