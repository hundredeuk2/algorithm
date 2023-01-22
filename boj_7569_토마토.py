import sys
from collections import deque
input = sys.stdin.readline

def bfs(map_list, q):
    while q:
        z,y,x = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            
            if 0 <= nx < m and 0<= ny < n and 0<= nz < h and map_list[nz][ny][nx] == 0:
                map_list[nz][ny][nx] = map_list[z][y][x] + 1
                q.append((nz,ny,nx))
                
m,n,h = map(int, input().split())
map_list = []
for _ in range(h):
    tmp = []
    for __ in range(n):
        tmp.append(list(map(int, input().split())))
    map_list.append(tmp)
    
dx, dy, dz = [1,-1,0,0,0,0], [0,0,-1,1,0,0],[0,0,0,0,-1,1]
q = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if map_list[i][j][k] == 1:
                q.append((i,j,k))
                
bfs(map_list,q)
result = 0
for h in map_list:
    for y in h:
        if 0 in y:
            print(-1)
            exit(0)
        result = max(result, max(y))
print(result-1)