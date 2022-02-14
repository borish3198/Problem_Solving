import sys

input = sys.stdin.readline

n = int(input())
data = {}

for _ in range(n):
  line = list(map(str, input().split()))
  data[line[0]] = line[1:]


sort_1 = dict(sorted(data.items()))
sort_2 = dict(sorted(sort_1.items(), key = lambda x:int(x[1][2]), reverse=True))
sort_3 = dict(sorted(sort_2.items(), key = lambda x:int(x[1][1])))
sort_4 = dict(sorted(sort_3.items(), key = lambda x:int(x[1][0]), reverse=True))

for name in sort_4.keys():
  print(name)
  
  
  ****************************************************************************************************************************
  
  students = []
  for i in range(n):
    students.append(input().split())
    
  students.sort(key= lambda x : (-int(x[1]), int(x[2]), -int(x[3]), int(x[0]))
                 
