# 문제의 조건에 입력값이 '자연수'로 한정
# 계수정렬을 이용해 문제 해결 가능하다.
# 입력값을 input()함수로 실행했을 때 시간초과 문제 발생
# 해당부분을 sys라이브러리의 stdin.readline()으로 수정하니 문제가 해결되었다.
# 앞으로 입력을 input함수 대신 sys.stdin.readline()으로 받아야 겠다.

import sys
g = [0]*10001

for i in range(int(input())):
  g[int(input())]+=1
'''
for i in range(int(sys.stdin.readline())):
  g[int(sys.stdin.readline())]+=1
'''
for i in range(10001):
  for j in range(g[i]):
    print(i)

'''
input()과 가장 큰 차이점은 input() 은 내장 함수로 취급되는 반면 sys 에 속하는 메소드들은 file object로 취급된다. 

즉, 사용자의 입력만을 받는 buffer를 하나 만들어 그 buffer에서 읽어들이는 것이다.

input()은 더 이상 입력이 없는데도 수행될 경우 EOFerror를 뱉어내는 반면 sys.stdin.readline()은 빈 문자열을 반환한다. 어떻게 보면 에러에서도 안전할 듯?
'''
