def solution(progresses, speeds):
    answer = []
    work = [] # 진도가 100이 되는데 걸리는 일 수 저장
    function = 1 
    for i in range(len(progresses)):
        cnt = 0 # 진도가 100이 되는데 걸리는 일 수
        while progresses[i] < 100: # 진도 100될 때까지 speeds 더해 줌
            progresses[i] += speeds[i]
            cnt += 1
        work.append(cnt)    
        
        if len(work) >= 2: 
            if work[i-1] >= work[i]: # 앞에 기능 배포가 뒤에 기능 배포보다 늦으면
                function += 1 # 앞에 기능과 같이 배포해야하므로 +1
                work[i-1], work[i] = work[i], work[i-1] 
                # 배포가 더 오래걸리는 기능과 다음기능을 비교해야 배포 여부 파악이 가능하므로 자리 바꿈
            else: # 앞에 기능 배포가 뒤에 기능 배포보다 빠르면
                answer.append(function)  
                function = 1 
    answer.append(function) # 마지막 기능 배포 표시를 위해서
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))