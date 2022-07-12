num = int(input())
arr = list(map(int, input().split()))
sumList = []
sumList.append(arr[0])

for i in range(1,num):
   if sumList[i-1] < 0:
       sumList.append(max(arr[i], sumList[i-1]+arr[i]))
   else:
       sumList.append(sumList[i-1]+arr[i])     
       
print(max(sumList))       