a, b, v = map(int,input().split())
k = (v-b)/(a-b) # a*k - b*(k-1) >= v 변형
if k == int(k):
    print(int(k))
else:
    print(int(k)+1)