def solution(s):
    answer = 1001
    
    if len(s)==1:
      return 1
    for i in range(1, (len(s)//2)+1):
        prev = ''.join(s[0:i])
        cnt = 1
        text = []
        for j in range(1, (len(s)//i)+1):          
            k = j*i
            word = s[k:k+i]
            if word == prev:
                cnt+=1
            else:
                if cnt==1:
                    text.append(prev)
                else:
                    text.append(str(cnt)+''.join(prev))
                cnt=1
                prev = word
        for j in range(len(s)-(len(s)%i), len(s)):
            text.append(s[j])
        temp = ''.join(text)
        print(temp)
        if answer>len(temp):
            answer = len(temp)

    return answer
  
s = input()

solution(s)
