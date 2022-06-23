num = int(input())
i = 1
while num > i:
    num -= i
    i += 1

if i % 2 == 0:
    a = num
    b = i-num+1
elif i % 2 == 1:
    a = i-num+1
    b = num

print(a,'/',b,sep="")    
