number = set(range(1,10001))
notSelfNum = set()

for i in range(1,10001):
    generater = i
    for j in str(i):
        generater += int(j)
    notSelfNum.add(generater)
    
result = number - notSelfNum
result = sorted(result)

for k in range(len(result)):
    print(result[k])