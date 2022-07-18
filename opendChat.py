def solution(record):
    useId = {}
    answer = []
    for i in range(len(record)):
        userId = record[i].split(" ")[1]
        if "Enter" in record[i]:
            nickname = record[i].split(" ")[2]
            useId.setdefault(userId,nickname)
            if userId in useId:
                useId[userId] = nickname
        elif "Change" in record[i]:
            nickname = record[i].split(" ")[2]
            useId[userId] = nickname
            
    for j in range(len(record)):
        userId = record[j].split(" ")[1]
        if "Enter" in record[j]:
            enter = str(useId.get(userId))+"님이 들어왔습니다."
            answer.append(enter)
        elif "Leave" in record[j]:
            leave = str(useId.get(userId))+"님이 나갔습니다."
            answer.append(leave)    
               
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))