def gcd(w,h): #최대공약수 구하는 함수
    for i in range(min(w,h),0,-1):
        if w%i == 0 and h%i == 0:
            break
    return i    

def solution(w,h):
    answer = 1
    if w == h: #정사각형이면 변의 길이가 사각형 개수
        answer = w*h - w
    elif w == 1 or h == 1: #한 변 길이가 1이면 다른 변의 길이가 사각형 개수
        answer = w*h - max(w,h)
    else: #나머지 경우, 두 변의 길이의 합에서 두 변의 길이의 최대공약수를 뺀 것이 사각형 개수
        answer = w*h - (w+h-gcd(w,h))
    return answer


w = 8
h = 12
print(solution(w,h))