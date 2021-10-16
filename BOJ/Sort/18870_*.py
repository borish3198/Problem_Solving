'''
1. 집합 자료형을 통해 중복값을 없앤 아이디어 까지는 좋았음
2. 축소된 좌표값의 값을 구하기 위해 index함수를 썼으나, 시간복잡도(n^2)으로 시간초과
3. 이런 때 딕셔너리 자료형을 통해 손쉽게 문제 해결 가능
4. 추가로 리스트, 딕셔너리 표현식, enumerate 함수로 코드를 단축시킬 수 있다는 점 
'''

import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data2 = list(set(data))
data2.sort()
data3 = {v:i for i, v in enumerate(data2)}
for i in data:
    print(data3[i], end=' ')
