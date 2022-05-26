def solution(p):
    
    if len(p) == 0:
        return p
    
    u, v = split(p)
    
    if check(u):
        return u + solution(v)

    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        
        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
                
        return answer
                
def split(p):
    lcnt = 0
    rcnt = 0
    i=0
    while i < len(p):
        if p[i:i+1] == '(':
            lcnt += 1

        if p[i:i+1] == ')':
            rcnt += 1      
        i+=1
        
        if lcnt == rcnt:
           return p[:i], p[i:]        
       
def check(u):
    stk = []
    
    for i in range(len(u)):
        if u[i:i+1] == '(':
            stk.append(u[i:i+1])
        else:
            if len(stk) == 0:
                return False
            stk.pop()
    return True     