'''
반례를 생각해내는게 중요하다는 점을 깨달은 문제
최장거리 수열 문제를 스스로 생각했다는 점 고무적!
'''

n = int(input())
data = list(map(int, input().split()))

a = [1 for _ in range(n)]

for i in range(n):
    temp=0
    for j in range(0, i):
        if data[j] < data[i]:
            temp = max(a[j], temp)
    a[i]=temp+1

print(max(a))
