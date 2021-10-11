# 입력받은 값을 오름차순으로 정렬하는 간단한 프로그램
# 연습차원에서 선택정렬로 구현, O(n^2) 시간복잡도를 가진다.
# 데이터 값이 10,000개가 넘어갈 경우 수행 시간이 급격히 느려진다.

data = [int(input()) for _ in range(int(input()))]

def s_sort(graph):
    for i in range(len(graph)):
        min = i
        for j in range(i+1, len(graph)):
            if graph[j]<graph[min]:
                graph[j], graph[min] = graph[min], graph[j]
    for i in range(len(graph)):
        print(graph[i])

s_sort(data)
