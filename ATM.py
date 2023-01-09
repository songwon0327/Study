waiter = int(input())
waitTime = list(map(int, input().split()))
tsum = 0
total = 0

waitTime = sorted(waitTime)

for i in range(waiter):
    tsum = tsum + waitTime[i]
    total = total + tsum

print(total)    