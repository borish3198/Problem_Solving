# 하노이의 탑 문제
# 원판이 움직이는 일반적인 원칙을 찾기까지 시간이 오래 걸렸다.
# 문제 풀 때 찾은 조건은 두 가지
# 1. 원판은 자기보다 한 사이즈 큰 원판이 가고자 하는 곳으로 가면 안된다.
# 2. 원판은 자기가 있던 곳으로 가지 않는다.(최소거리)
# 19열의 return을 작성함으로써 코드 완성. 

def pyramid(n, a, location):

    if n==1:
        print(location[n-1], a)
        location[n-1] = a
        return

    else:
        while n>1:
            if location[n-1]==a:
                pyramid(n-1, a, location)
                return
            else:
                n_a = 6-location[n-1]-a
                pyramid(n-1, n_a, location)
                print(location[n-1], a)
                location[n-1] = a


location = []
n = int(input())
for i in range(n):
    location.append(1)
print(pow(2,n)-1)
pyramid(n, 3, location)
