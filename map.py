def solution(n, arr1, arr2):
    answer = []
    arr3 = []
    for i in range(n):
        arr1[i] = format(arr1[i],'b')
        arr1[i] = arr1[i].zfill(n)
        arr2[i] = format(arr2[i],'b')
        arr2[i] = arr2[i].zfill(n)
        arr3.append(int(arr1[i])+int(arr2[i]))
        arr3[i] = str(arr3[i]).zfill(n)
        answer.append(arr3[i].replace('0',' ').replace('1','#').replace('2','#'))
    return answer

n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))