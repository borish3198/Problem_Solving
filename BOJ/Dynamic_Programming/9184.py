import sys
input = sys.stdin.readline

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        if data[a+50][b+50][c+50]:
            return data[a+50][b+50][c+50]
        else:
            data[a+50][b+50][c+50]=1
            return 1

    if a > 20 or b > 20 or c > 20:
        if data[70][70][70]:
            return data[70][70][70]
        else:
            data[70][70][70]=w(20, 20, 20)
            return data[70][70][70]
            
    if a < b and b < c:
        if data[a+50][b+50][c+50]:
            return data[a+50][b+50][c+50]
        else:
            data[a+50][b+50][c+50]=w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return data[a+50][b+50][c+50]     
            
    else:
        if data[a+50][b+50][c+50]:
            return data[a+50][b+50][c+50]
        else:
            data[a+50][b+50][c+50]=w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)        
            return data[a+50][b+50][c+50]

data = [[[0]*(101) for _ in range(101)] for _ in range(101)]


while True:
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    ans = w(a,b,c)
    print("w(%i, %i, %i) = %i" %(a, b, c, ans))
