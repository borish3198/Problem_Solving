import sys

input = sys.stdin.readline

def binary(start, end):
    if start>end:
        return -1

    mid = (start+end)//2

    if mid == data[mid]:
        return mid
    elif mid > data[mid]:
        return binary(mid+1, end)
    else:
        return binary(start, mid-1)



n = int(input())
data = list(map(int, input().split()))

print(binary(0, n-1))
