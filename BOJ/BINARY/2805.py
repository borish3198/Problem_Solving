'''
Q. 이진탐색 구현시 재귀함수가 while 반목문 보다 빠른 이유는?
'''

import sys

n, m = map(int, sys.stdin.readline().split())
lan = sorted(list(map(int, sys.stdin.readline().split())))

def binary(data, target, start, end):
    result=None
    while start<=end:
        mid = (start+end)//2
        sum = 0
        for i in data:
            if mid<=i:
                sum+=(i-mid)
        if target == sum:
            result = mid
            break
        elif target > sum :
            end = mid-1
        else:
            result = mid
            start = mid+1
    return result

print(binary(lan, m, 0, lan[-1]))
