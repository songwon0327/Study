#letter = "A"

#for i in range(count):
#    letter = letter.replace("A","b").replace("B","BA")
#    letter = letter.upper()
#A = letter.count("A")
#B = letter.count("B")
#print(format(A)+format(" ")+format(B))        
#메모리 초과 피보나치로 풀어야함

count = int(input())
cnt = [0]*(count+1)

cnt[1] = 1

for i in range(2,count+1):
    cnt[i] = cnt[i-1]+cnt[i-2]
    
print(cnt[count-1], cnt[count])    