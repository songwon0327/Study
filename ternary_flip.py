def solution(n):
    answer = ''
    
    while n > 0:
        mod = n%3
        n = n//3
        answer = answer + str(mod)
    return int(answer,3)

#print(solution(45))