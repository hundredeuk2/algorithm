import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
y, x, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서 (반시계방향 90도 로테이트)
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

count = 0

def rotate_left(d):
    return (d + 3) % 4

def backward(d):
    return (d + 2) % 4

def dfs(y, x, d):
    global count

    # No.1 order
    if room[y][x] == 0:
        room[y][x] = -1
        count += 1

    # 2,3 order condition check
    for _ in range(4):
        d = rotate_left(d)
        ny = y + dy[d]
        nx = x + dx[d]
        if room[ny][nx] == 0:
            dfs(ny, nx, d)
            return 

    # No.2 order
    back_d = backward(d)
    ny = y + dy[back_d]
    nx = x + dx[back_d]

    if room[ny][nx] != 1:
        dfs(ny, nx, d)
    else:
        return
    
dfs(y, x, d)
print(count)
