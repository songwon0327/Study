value, price = map(int, input().split())
moneyList = []
cnt = 0

for i in range(value):
    money = int(input())
    moneyList.append(money)

for j in reversed(range(value)):
    if price >= moneyList[j]:
        cnt += price // moneyList[j]
        price = price % moneyList[j]
    if price == 0:
        break
    
print(cnt)        
            