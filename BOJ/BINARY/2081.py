import sys

n = sys.stdin.readline()
data = []
sum=0

for i in range(n):
    k=sys.stdin.readline()
    sum+=k
    data.append(k)

average = round(sum/n)
data.sort()
mid = data[n//2]
diff = data[-1]-data[0]
num=0
max=0
for i in range(n-1):
    if data[i]==data[i+1]:
        num+=1
    else:
        if num+1>max:
            max=num+1
            num=0
            
print(average)    
print(mid)
print(max)
print(diff)
