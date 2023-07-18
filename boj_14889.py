import sys
input = sys.stdin.readline

def backtracking(idx, cnt):
    global answer
    if cnt == n // 2:
        cal()
        return
    if idx >= n:
        return
    player[idx] = 1
    backtracking(idx + 1, cnt + 1)
    player[idx] = 0
    backtracking(idx + 1, cnt)

def cal():
    s = []
    l = []
    for i in range(n):
        if player[i] == 0:
            s.append(i)
        else:
            l.append(i)
    s_s = sum(matrix[i][j] for i in s for j in s)
    l_s = sum(matrix[i][j] for i in l for j in l)
    global answer
    answer = min(answer, abs(s_s - l_s))

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
player = [0] * n
answer = float('inf')

backtracking(0, 0)
print(answer)