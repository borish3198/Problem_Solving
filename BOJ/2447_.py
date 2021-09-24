# 백준 2447번 별찍기
# 한창 백준 단계별로 풀어보기를 통해 코딩에 열을 올리던 중 장차 4개월 간 나를 코딩에서 손 놓게 한 장본인
# 나만의 풀이를 찾았지만 '시간초과'로 오답
# 여러 풀이가 있지만 그중에서도 가장 재귀함수에 성격에 맞고 간결한 풀이를 가져옴
# 1년 뒤에는 이런 코드를 떠올릴 수 있을지..

import sys

def star(row, col, sz):
    if sz == 1:
        a[row][col] = '*'
        return
    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                star(row + sz // 3 * i, col + sz // 3 * j, sz // 3)

n = int(input())
a = [[' ']*n for i in range(n)]
star(0, 0, n)

for i in range(n):
    for j in range(n):
        sys.stdout.write(a[i][j])
    sys.stdout.write('\n')
