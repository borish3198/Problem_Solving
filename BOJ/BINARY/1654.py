'''
교재의 떡 자르기 문제와 유사한 문제
최적화 된 값을 찾기 위한 문제(parametic search)는 이진탐색을 활용할 것
* 해당 문제를 풀면서 실제 코딩 테스트 때는 얼마나 많은 것들을 고려해야 해나 정리할 필요를 느낌
- 이진탐색에서 초기 시작값과 끝값 설정에 대해 좀 더 숙고할 것
- zerodivision error 발생 : 0으로 나누게 되는 경우는 없는지 사전에 판단
- unboundlocal error 발생 : 0으로 나누게 될 경우 예외처리는 어떻게 할 것인지
'''


import sys

n, m = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(n)]

def binary(data, target, start, end):
    while start<=end:
        mid = (start+end)//2
        sum = 0
        extra = 0
        for i in data:
            if mid!=0:
                sum+=(i//mid)
                extra+=(i%mid)
            else:
                result = 0
        if target == sum and extra==0:
            result = mid
            break
        elif target > sum :
            end = mid-1
        else:
            result = mid
            start = mid+1
    return result

print(binary(lan, m, 1, max(lan)))
