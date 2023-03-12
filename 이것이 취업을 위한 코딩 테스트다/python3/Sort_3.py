# 행렬 A, B에서 원소를 K번 교환할 수 있을 때 A의 합의 최댓값을 구하는 프로그램

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
    A[i] = B[i]

print(sum(A))
