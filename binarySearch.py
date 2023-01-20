def binarySearch(target, aList):
    left = 0
    right = a-1
    
    while left <= right:
        mid = (left + right) // 2
        
        if aList[mid] == target:
            return 1
        elif aList[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return 0       

a = int(input())
aList = sorted(list(map(int,input().split())))
b = int(input())
bList = list(map(int,input().split()))


for i in range(b):
    print(binarySearch(bList[i], aList))
        