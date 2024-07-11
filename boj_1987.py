import sys
input = sys.stdin.readline

r, c = map(int, input().split())
pan = [input().strip() for _ in range(r)]

answer = 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def find(x, y, cnt, bitmask):
    global answer
    
    answer = max(cnt, answer)
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < r and 0 <= ny < c:
            idx = ord(pan[nx][ny]) - ord('A')
            if not (bitmask & (1 << idx)):
                find(nx, ny, cnt + 1, bitmask | (1 << idx))

initial_bitmask = 1 << (ord(pan[0][0]) - ord('A'))
find(0, 0, 1, initial_bitmask)
print(answer)