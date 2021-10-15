# 배열을 연속된 문자열로 변환하는 법을 알 수 있음
# 문자열의 join 메소드 활용하여 해결 가능
# 배열의 원소가 정수일 경우 문자로 변환하여야 새로운 문자열로 결합 가능

data = list(map(int, input()))
data.sort(reverse=True)
answer = "".join(str(_) for _ in data)
print(answer)
