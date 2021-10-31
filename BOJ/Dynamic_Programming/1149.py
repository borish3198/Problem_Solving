'''
d = [[0,0,0]]*n+1
이 방법으로 배열을 선언하게 되면, 단순히 요소를 복사하게 되는 얕은복사 (shallow copy)가 일어난다. 
단순히 요소를 복사하다 보니 바라보는 객체는 동일하다. 즉, 이러한 방식으로 선언 뒤에, 
값을 변경하게되면 다른 원소들도 값이 변경되는 현상이 발생하게 되므로 이를 인지하고, 
후에 대입연산자를 통해 값을 변경하지 않는 경우에만 사용하는것이 좋다.
'''

n = int(input())
rgb = [[0,0,0]]
d = [[0 for _ in range(3)] for _ in range(n+1)]

for i in range(n):
    rgb.append(list(map(int, input().split())))

for i in range(1, n+1):
    d[i][0] = rgb[i][0] + min(d[i-1][1], d[i-1][2])
    d[i][1] = rgb[i][1] + min(d[i-1][0], d[i-1][2])
    d[i][2] = rgb[i][2] + min(d[i-1][0], d[i-1][1])

print(min(d[n]))
