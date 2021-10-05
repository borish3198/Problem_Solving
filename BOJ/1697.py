# 숨바꼭질 문제
# 문제 해결 접근은 나쁘지 않았으나 마무리까지가 아쉬움
# 1. n이 k보다 큰 경우 - 무조건 -1씩 움직일 수 있으므로 불필요한 연산을 제거하기 위한 조건문 추가 -> 여전히 시간 초과 문제
# 2. visited 리스트의 맹점 - 리스트에서 특정값을 찾는데 걸리는 시간이 꽤 오래 걸린다는 사실을 깨달음 -> 입력값 범위 만큼의 빈 리스트를 만들어, index를 통해 접근
# 3. runtime error(index) - 기초적인 실수이지만 처음부터 떠올리기는 쉽지 않다. 주의할 것!

from collections import deque

n, k = map(int, input().split())

def bfs(n, k):
    if n>k:
        return(n-k)
    count=0
    queue = deque()
    visited = [0]*100001
    dx = [1, -1]
    queue.append((k, count))
    visited[k]=1
    while queue:
        r, count = queue.popleft()
        if r==n:
            return count
        for i in range(2):
            n_r = r+dx[i]
            if n_r>=0 and n_r<=100000 and visited[n_r]==0:
                queue.append((n_r, count+1))
                visited[n_r]=1
        if r%2==0:
            n_r = int(r/2)
            if visited[n_r]==0:
                queue.append((n_r, count+1))
                visited[n_r]=1
print(bfs(n, k))
