num = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
total = 0
multi = 0

a.sort()
b.sort(reverse=True)

for i in range(num):
    multi = a[i]*b[i]
    total += multi
    
print(total)