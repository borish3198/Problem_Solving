from itertools import permutations
import copy

def dfs(temp, i, j, direction):
    dx = [0, -1, 0, 1, 0]
    dy = [0, 0, +1, 0, -1]
    if temp[i][j] == "O":
        return True
    elif temp[i][j] == "T":
        return False
    else:
        if direction == 0:
            for k in range(1, 5):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx>=0 and nx<n and ny>=0 and ny<n:
                    ans = dfs(temp, nx, ny, k)
                    if not ans:
                        return False
            
        else:
            nx = i + dx[direction]
            ny = j + dy[direction]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                ans = dfs(temp, nx, ny, direction)
                if not ans:
                    return False

        return True
    

n = int(input())
data = [list(map(str, input().split())) for _ in range(n)]
empty = []
student = []

for i in range(n):
    for j in range(n):
        if data[i][j] == "X":
            empty.append((i,j))
        elif data[i][j] == 'S':
            student.append((i,j))

comb = list(permutations(empty, 3))

for case in comb:
    ans = 0
    temp = copy.deepcopy(data)
    for i, j in case:
        temp[i][j] = "O"

    for x, y in student:
        ans_3 = dfs(temp, x, y, 0)
        if ans_3:
            ans+=1
    # print("ans: ", ans)
    if ans == len(student):
        # for i in range(n):
        #     for j in range(n):
        #         print(temp[i][j], end=" ")
        #     print()
        break

if ans == len(student):
    print("YES")
else: print("NO")

