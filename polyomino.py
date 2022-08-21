board = input()
answer = ""
    
dot = board.replace("X"," ")
dotList = dot.split(" ")
dotList = list(filter(None, dotList)) # "."만 분리해서 저장한 리스트

X = board.replace("."," ")
XList = X.split(" ")
XList = list(filter(None,XList)) # "X"만 분리해서 저장한 리스트

for i in range(len(XList)):
    if len(XList[i]) % 2 == 0: #"X"가 짝수면 폴리오미노 생성 가능
        if len(XList[i]) % 4 == 0: #4의 배수면 전부 A
            XList[i] = XList[i].replace("X","A")
        elif len(XList[i]) == 2: #2일 때만 전부 B
            XList[i] = XList[i].replace("X","B")    
        else: #나머지 경우는 4로 나눈 몫 만큼 A로 나머지는 B
            partA = (len(XList[i]) // 4)*4
            XList[i] = XList[i][:partA].replace("X","A") + XList[i][partA:].replace("X","B")    
    else: #X가 홀수면 폴리오미노 불가능
        answer = "-1"
        break  
    
if answer == "": #폴리오미노 가능한 경우에 "."이랑 바꾼 XList 합침
    for i in range(min(len(XList), len(dotList))):
        if board[:1] == "X":
            answer = answer + XList[i] + dotList[i] 
        else:
            answer = answer + dotList[i] + XList[i]
            
    if len(XList) < len(dotList):
        answer += dotList[-1]   
    elif len(XList) > len(dotList):
        answer += XList[-1]      
        
if (answer.count("A") + answer.count("B") + answer.count(".")) < len(answer): #"X"랑 "." 말고 다른 문자 입력될 시 -1 처리
    answer = "-1"
    
print(answer)