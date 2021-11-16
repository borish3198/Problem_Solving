'''
2주동안 좌절하게 한 문제, 결국 문제를 풀지 못함.
문제를 풀 때 처음 접근한 방법에 고착되어 문제를 완전히 다른 방향으로 접근하지 못하고 있음.
이 문제에서도 연속되는 계단을 flag 값으로 유지하려 했던 것이 화근..
점화식은 더 단순한 형태로 표현된다는 점에 유념하여 여러 방면의 접근을 고민해보자
'''


n = int(input())
stair = [0]
stair += [int(input()) for _ in range(n)]
data = [0]*(n+1)

if n==1:
    print(stair[1])
elif n==2:
    print(stair[1]+stair[2])

else:
    data[1] = stair[1]
    data[2] = stair[2] + stair[1]
    flag = 1
    for i in range(3, n+1):
        data[i] = stair[i] + max(data[i-2], data[i-3]+stair[i-1])

    print(data[n])
