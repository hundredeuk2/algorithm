answer = 1e9

def bt(start, cnt, visitied, target,words):
    if start == target:
        global answer
        answer = min(answer, cnt)
        return

    for i in range(len(words)):
        if visitied[i]:
            continue
        tmp_cnt = 0
        for j in range(len(start)):
            if tmp_cnt > 1:
                break
            if start[j] != words[i][j]:
                tmp_cnt += 1
        if tmp_cnt==1:
            visitied[i] = True
            words[i]
            bt(words[i], cnt+1, visitied,target,words)
            visitied[i] = False

def solution(begin, target, words):
    visitied = [False for _ in range(len(words))]
    if target not in words:
        return 0
    bt(begin, 0, visitied, target, words)
    return answer