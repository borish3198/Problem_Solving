'''
문제 풀이에 대한 접근은 맞았으나 생각을 구현하지 못한 사례
코딩 실력의 한계를 절감하는 문제
'''


import heapq

def solution(food_times, k):
    
    if sum(food_times)<=k:
        return -1
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i], i+1))

    sum_value = 0
    previous = 0
    
    length = len(food_times)
    
    while sum_value + ((q[0][0]-previous)*length)<=k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous)*length
        length -= 1
        previous = now
    
    result = sorted(q, key =lambda x: x[1])
    return result[(k-sum_value)%length][1]
