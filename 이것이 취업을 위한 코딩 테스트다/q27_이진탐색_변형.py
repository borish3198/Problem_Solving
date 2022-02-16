import sys

input = sys.stdin.readline

n, x = map(int, input().split())
data = list(map(int, input().split()))

def count_x(target, n):
    start_idx = find_start(0, n-1, target)
    print(start_idx)
    if start_idx == None:
        return -1

    end_idx = find_end(0, n-1, target)
    print(end_idx)
    if end_idx == None:
        return -1

    ans = end_idx - start_idx +1
    return ans

def find_start(start, end, target):
    if end<start:
        return None
    
    mid = (end+start)//2
    if (mid==0 or data[mid-1]<target) and data[mid] == target:
        return mid

    elif data[mid] >= target:                               # 해당 조건문에서의 조건식 '>=' 의미를 다시 생각해보기
        return find_start(start, mid-1, target)

    else:
        return find_start(mid+1, end, target)

def find_end(start, end, target):
    if end<start:
        return None
    
    mid = (end+start)//2
    if (mid==n-1 or data[mid+1]>target) and data[mid] == target :
        return mid

    elif data[mid] > target:                                # 해당 조건문에서의 조건식 '>' 의미를 다시 생각해보기
        return find_end(start, mid-1, target)

    else:
        return find_end(mid+1, end, target)   

print(count_x(x, n))
