def sumCycle(first, second, cnt):
    third = (first + second)%10
    nnum = (second*10) + third
    cnt+=1
    if nnum == num:
        print(cnt)
    else:
        sumCycle(second, third, cnt)
    return    

num = int(input())
first = num // 10
second = num % 10  
sumCycle(first, second, 0)