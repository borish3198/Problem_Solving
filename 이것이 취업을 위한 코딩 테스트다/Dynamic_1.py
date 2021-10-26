'''
네 가지 연산으로 1을 만드는 가장 작은 수를 찾는 알고리즘
다이나믹 프로그래밍 방법 중 bottom-up 방식을 통해 문제를 해결한다. 
'''

n = int(input())
data = [0]*(n+1)

for i in range(2, n+1):
    data[i] = data[i-1]+1
    if i%2==0:
        data[i] = min(data[i], data[i//2]+1)
    elif i%3==0:
        data[i] = min(data[i], data[i//3]+1)
    if i%5==0:
        data[i] = min(data[i], data[i//5]+1)    

print(data[n])
