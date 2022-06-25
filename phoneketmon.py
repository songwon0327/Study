def solution(nums):
    answer = 0
    setNums = set(nums)
    if (len(nums)//2) >= len(setNums):
        answer = len(setNums)
    else:
        answer = len(nums)//2  
    return answer

nums = [3,3,3,2,2,4]
print(solution(nums))