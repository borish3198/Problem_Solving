
import sys

n = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

def binary(data, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2
    if target==data[mid]:
        return mid
    elif target>data[mid]:
        return binary(data, target, mid+1, end)
    else:
        return binary(data, target, start, mid-1)

for i in B:
    result = binary(A, i, 0, n-1)
    if result==None:
        print(0)
        continue
    print(1)
