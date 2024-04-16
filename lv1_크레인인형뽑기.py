def solution(board, moves):
    answer = 0
    
    new_board = []
    for i in range(len(board)):
        tmp = []
        for j in range(len(board)-1,-1,-1):
            if board[j][i] == 0:
                continue
            tmp.append(board[j][i])
        new_board.append(tmp)
        
        
    q = []
    for num in moves :
        if len(new_board[num-1]) == 0:
            continue

        tmp = new_board[num-1].pop()
        if len(q) == 0:
            q.append(tmp)
            continue

        if q[-1] == tmp:
            q.pop()
            answer += 2
        else:
            q.append(tmp)
    return answer