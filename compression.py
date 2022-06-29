def solution(s):
    answer = 0
    length = []
    
    for i in range(1,len(s)//2+2):
        ss = ''
        num = 0
        cnt = 1
        for j in range(1,len(s)//i+1):
            if s[num:num+i] == s[num+i:num+2*i]:
                cnt+=1
            else:
                if cnt == 1:
                    ss += s[num:num+i]
                else:
                    ss += str(cnt)
                    ss += s[num:num+i]      
                cnt=1
            num = num+i
        if cnt == 1:    
            ss += s[num:num+i]
        else:
            ss += str(cnt)
            ss += s[num:num+i]      
             
        length.append(len(ss))
    answer = min(length)
    
    return answer           
     
s = "aabbaccc"    
print(solution(s))