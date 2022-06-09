a, b, c = map(int,input().split())

if b >= c:
    print("-1")

else:
    print(a//(c-b)+1) #손익분기점 구하는 공식, 단순히 반복문 이용 시 시간 초과 

