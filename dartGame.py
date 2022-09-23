import re

def solution(dartResult):
    answer = 0
    i = 0
    opp = [] #각 기회 결과를 나눠서 리스트에 저장
    val = [0,0,0] #각 기회의 점수를 저장
    while i < len(dartResult):
        if "*" in dartResult[i:i+4] or "#" in dartResult[i:i+4]: #스타상 또는 아차상일 경우
            if "10" in dartResult[i:i+2]: #점수가 10점일 경우
                opp.append(dartResult[i:i+4]) #opp에 4글자 잘라서 저장
                i += 4 
                continue
            opp.append(dartResult[i:i+3]) #점수가 한자리 숫자인 경우 
            i += 3
        else: #스타상, 아차상 X
            if "10" in dartResult[i:i+2]: #점수가 10점
                opp.append(dartResult[i:i+3])
                i += 3
                continue
            opp.append(dartResult[i:i+2]) #점수가 한자리 숫자
            i += 2
    
    for j in range(3):
        number = re.findall("\d+",opp[j]) #문자열에서 숫자만 추출하기 위한 re라이브러리 함수
        if "#" in opp[j]: #아차상인 경우
            if "S" in opp[j]:
                val[j] = int(number[0])*(-1)
            elif "D" in opp[j]:
                val[j] = (int(number[0])**2)*(-1)
            else:
                val[j] = (int(number[0])**3)*(-1)  
        elif "*" in opp[j]: #스타상인 경우
            if j != 0: #스타상이 나온게 첫 번째 기회가 아닌 경우
                val[j-1] = val[j-1]*2 #앞선 기회도 점수 두 배
            if "S" in opp[j]:
                val[j] = int(number[0])*2   
            elif "D" in opp[j]:
                val[j] = (int(number[0])**2)*2
            else:
                val[j] = (int(number[0])**3)*2
        else: #아차상, 스타상 X
            if "S" in opp[j]:
                val[j] = int(number[0])   
            elif "D" in opp[j]:
                val[j] = (int(number[0])**2)
            else:
                val[j] = (int(number[0])**3)
                
    for k in range(3):
        answer += val[k]   #모든 기회 점수의 합을 구함
                
    return answer

dartResult = "1D2S#10S"
print(solution(dartResult))