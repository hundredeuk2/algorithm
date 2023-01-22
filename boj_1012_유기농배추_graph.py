import sys
input = sys.stdin.readline

t = int(input())

def bfs(x,y):
    q = [[x,y]]
    while q:
        x, y = map(int, q.pop(0))
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<= nx < n and 0<= ny < m and map_list[nx][ny] == 1 :
                map_list[nx][ny] = 0
                q.append([nx, ny])
                
                
for _ in range(t):
    m, n, k = map(int,input().split())
    map_list = [[0] * m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    cab_list = []
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    
    for _ in range(k):
        y, x = map(int, input().split())
        map_list[x][y] = 1
        cab_list.append([x,y])
        
    cnt = 0    
    
    for coord in cab_list:
        x, y = coord[0], coord[1]
        if map_list[x][y] == 0:
            continue
        else:
            bfs(x,y)
            map_list[x][y] =0
            cnt += 1
    print(cnt)