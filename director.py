
import math #올림(ceil) 함수 쓰기 위한 라이브러리 선언
classroom = int(input()) #시험장 개수
cnt = 0 # 부감독관 인원

student = list(map(int,input().split())) #시험장 당 응시자 수
b, c = map(int, input().split()) #감시 가능 인원
    
for j in range(len(student)):
    if student[j] - b > 0: # 총감독관은 반드시 1명 있어야 하므로 (응시자 수 - 총감독관이 감시 가능한 인원)이 0보다 클 경우만 부감독관 필요
       cnt += math.ceil((student[j]-b)/c) # 부감독관 수 = (응시자수 - 총감독관 감시 가능 인원)/부감독관 감시 가능 인원의 올림
print(cnt+len(student))   
         