n, k = map(int,input().split())
circle = []
josephus = []
j = 0

for i in range(1,n+1):
    circle.append(i)
    
while len(circle) > 0 :
    if (j+k-1) < len(circle): #index가 list 범위 안
        josephus.append(circle.pop(j+k-1)) #pop이용하여 josephus에 추가
        j = j+k-1
    else: #index가 list 범위 밖
        j = j - len(circle) + (k-1)
        if j >= len(circle): # 조정 후에도 index가 list 범위 밖인 경우
            josephus.append(circle.pop(j%len(circle)))
            j = j%(len(circle)+1)
            continue
        josephus.append(circle.pop(j))
print("<" + ", ".join(list(map(str, josephus))) + ">")