num = int(input())

for i in range(num):
    cnt = 0
    quizSum = 0
    a = input()
    for j in range(len(a)):
        if a[j:j+1] == 'O':
            cnt += 1
            quizSum += cnt
        else:
            cnt = 0
            quizSum += cnt
    print(quizSum)            