'''
이진 탐색 문제의 변형
주어진 데이터 내에 특정 값이 몇 개 있는지를 출력하는 문제
총 3번 시도 2번 실패
#1 이진탐색 도중 타겟 값을 찾을 경우, 해당 데이터의 앞, 뒤로 몇 개의 동일한 값이 있는지를 탐색(재귀함수로 구현)
#2 딕셔너리 자료형으로 데이터 별 개수를 value 값으로 저장 후 (반복문으로 구현)
#3 딕셔너리 자료형 + 재귀함수로 구현(통과)

* 두번째 시도에서 이진탐색을 반목문으로 구현한 이유는, 반목문의 실행속도가 재귀함수보다 빠를 것으로 기대했기 때문이나
  오히려 반목문으로 구현한 이진탐색이 시간초과가 뜸.
'''

import sys

n = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
dic = {i:0 for i in A}
for i in A:
    dic[i]+=1
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

def binary(data, target, start, end):
    if start>end:
        return 0
    mid = (start+end)//2
    if target==data[mid]:
        return dic[target]

    elif target>data[mid]:
        return binary(data, target, mid+1, end)
    else:
        return binary(data, target, start, mid-1)

for i in B:
    result = binary(A, i, 0, n-1)
    print(result, end=' ')
