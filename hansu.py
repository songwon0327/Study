num = int(input())
han = 0
hanList = []

if num < 100:
    han = num
else:
    for i in range(100,num+1):
        hanList.clear()
        for j in str(i):
            hanList.append(int(j))    
        if hanList[1] - hanList[0] == hanList[2] - hanList[1]:
            han += 1
    han += 99
    
print(han)         