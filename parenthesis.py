num = int(input())
cnt = 0
for i in range(num):
    pare = input()
    for k in range(len(pare)):
        if cnt < 0:
            break
        if pare[k:k+1] == "(":
            cnt += 1
        else:
            cnt -= 1   
    if cnt == 0:
        print("YES")
    else:
        print("NO")          