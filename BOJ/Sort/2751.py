# 계수정렬을 통해 문제 해결
# 입력값 절댓값 1,000,000(백만) 이하의 정수
# 음수를 포함할 수 있는 길이의 리스트 선언 후 계수 정렬 구현

import sys
n = int(sys.stdin.readline())
g = [0]*2000001

for i in range(n):
    k = int(sys.stdin.readline())
    g[k+1000000] += 1

for i in range(2000001):
  if g[i]:
      print(i-1000000)
