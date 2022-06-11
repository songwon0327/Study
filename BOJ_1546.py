num = int(input())
score = list(map(int,input().split()))
score.sort(reverse=True)

sum = 0
nscore = []
for i in range(len(score)):
    nscore.append(score[i]/score[0]*100)
    sum += nscore[i]
ave = sum/num
print(ave)