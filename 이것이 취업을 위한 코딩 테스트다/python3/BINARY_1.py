import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
order = list(map(int, sys.stdin.readline().split()))

def binary(data, target, start, end):
    if start>end:
        return -1
    mid = (start+end)//2
    if data[mid] == target:
        return mid+1
    elif data[mid]>target:
        return binary(data, target, start, mid-1)    
    else:
        return binary(data, target, mid+1, end)
    
for i in range(m):
    result = binary(data, order[i], 0, n-1)
    if result==-1:
        print("no", end=" ")
        continue
    print("yes", end=" ")

