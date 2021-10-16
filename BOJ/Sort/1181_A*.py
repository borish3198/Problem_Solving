'''
할 이야기가 많은 문제이다.
1. 주어지는 데이터값이 2만개 이하로 선택정렬을 통해 구현 가능하다고 판단하여 코드 작성하였으나, 시간초과
2. 삽입정렬의 경우 어느정도 정돈된 데이터의 경우 시간복잡도가 n에 수렴하여, sort함수로 단어의 길이에 대한 정렬 이후 삽입정렬하였으나, 시간초과
3. 단어의 글자수를 저장하는 리스트를 만들어 단어수가 겹치는 부분만 삽입정렬 시도했으나, 시간초과
4. 문제 풀이를 참고하니 단어의 알파벳 순으로 정렬한 이후 단어의 길이로 정렬하는 간단한 방법으로 해결하더라..
* 데이터값을 정렬하는 조건이 여러개일 때 이를 한번에 복잡하게 구현하려 하지 말고 순서를 바꾸는 고민을 하자.
'''

import sys
n = int(sys.stdin.readline())
data = []

for i in range(n):
    word = list(map(str, sys.stdin.readline()))
    if word in data:
        continue
    data.append(word)

data.sort()
data.sort(key=lambda x:len(x))

for i in data:
    word = "".join(i[:-1])
    print(word)
