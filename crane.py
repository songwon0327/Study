def solution(board, moves):
    box = [] #인형을 담을 리스트
    answer = 0
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] == 0: # 인형이 없을 때 
                continue
            else: # 인형이 있을 때
                doll = board[j][moves[i]-1]
                box.append(doll) #box 리스트에 인형 추가
                board[j][moves[i]-1] = 0 # 뽑은 인형은 0으로 변경
                if len(box) >= 2 and box[-1] == box[-2]: # box리스트에 인형이 두 개 이상 있고 같은 인형이 연달아 있는 경우
                    del box[-1]
                    del box[-1] #연달아 있는 인형 삭제
                    answer += 2 #인형 두 개 삭제
                break
                
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))