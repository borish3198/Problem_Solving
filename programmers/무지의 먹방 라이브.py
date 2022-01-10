"""
2019 KAKAO BLIND RECRUITMENT 문제풀이
- 정확도 테스트 통과
- 효율성 테스트 실패
* 문제를 잘못읽어 두 시간을 낭비함
"""


def solution(food_times, k):
    
    menu = len(food_times)
    idx = 0
    z_count = 0
    while True:
        if k == -1:
            break
        if z_count==menu:
            answer=-2
            break
        if food_times[idx%menu]>0:
            z_count=0
            answer = idx%menu
            food_times[idx%menu]-=1
            k-=1
        else:
            z_count+=1
        idx+=1

    return answer+1 
