weight = int(input()) #설탕 총 무게
cnt = 0

while weight >= 0: 
    if weight % 5 == 0: #설탕 무게가 5의 배수일 경우 
        cnt += weight // 5 #5로 나눈 몫이 봉지 수
        break
    weight -= 3 #설탕 무게가 5의 배수가 되거나 0보다 작아질 때까지 
    cnt += 1 # 봉지 + 1
    
if weight < 0: # 3, 5kg로 나누어 떨어지지 않는 경우
    print("-1")    
else:
    print(cnt)    