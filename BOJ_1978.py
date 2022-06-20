import math

def prime(number):
    if number == 1:
      return False
    for j in range(2, int(math.sqrt(number))+1):
        if number%j == 0:
            return False
    return True    

num = int(input())
numbers = list(map(int,input().split()))
check = 0

for i in range(num):
    if prime(numbers[i]) == True:
        check += 1

print(check)        
        
    
