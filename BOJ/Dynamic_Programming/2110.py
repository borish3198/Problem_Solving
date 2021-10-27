'''
피보나치 수열의 변형 문제, DP bottom up 방식으로 해결함
*bottom up 방식을 사용할 경우 index_error를 주의할 것
'''

n = int(input())
d = [int(input()) for _ in range(n)]
m = [[0,0]]*41

m[0] = [1, 0]
m[1] = [0, 1]

for i in range(2, max(d)+1):
    m[i] = [m[i-2][0]+m[i-1][0], m[i-2][1]+m[i-1][1]]

for i in d:
    print(m[i][0], m[i][1])
