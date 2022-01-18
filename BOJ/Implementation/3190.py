import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
apple = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
shift = {}

for i in range(l):
    a, b = map(str, input().split())
    shift[a] = b

board = [[-1]*(n) for _ in range(n)]
for x, y in apple:
    board[x-1][y-1] = -10

answer = 0
dir = 0
time = 0
length = 1
head = [0,0]
mov = [[0,1], [+1,0], [0,-1], [-1,0]]

while True:
    # 1초 시간 경과에 따른 뱀의 머리 이동
    time+=1

    head[0] += mov[dir][0] 
    head[1] += mov[dir][1]

    # 머리가 이동한 곳이 벽 밖인지 체크
    if head[0]<0 or head[0]>=n or head[1]<0 or head[1]>=n:
        answer = time
        broke = True
        break 

    # 머리가 새로 이동한 곳에 사과가 있는지 확인
    new_place = board[head[0]][head[1]]
    if new_place == -10:
        length += 1

    # 머리가 새로 이동한 곳에 뱀의 신체가 남아있는지 확인    
    elif new_place>=time-length:
        answer = time
        break

    # 머리가 지나간 부분을 지나갔을 때 시간으로 최신화
    board[head[0]][head[1]] = time

    if str(time) in shift.keys():
        b = shift[str(time)]
        if b == "D":
            dir = (dir+1)%4
        else:
            dir = (dir+3)%4                

print(answer)

