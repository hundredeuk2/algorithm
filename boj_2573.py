from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def get_max_idx(map_list, n, m):
    max_idx = (0, 0)
    for i in range(n):
        for j in range(m):
            if map_list[i][j] > map_list[max_idx[0]][max_idx[1]]:
                max_idx = (i, j)
    return max_idx

def melt(map_list, n, m):
    next_map = [row[:] for row in map_list]  # 원본 보호용 복사
    for i in range(n):
        for j in range(m):
            if map_list[i][j] > 0:
                sea = 0
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if 0 <= ni < n and 0 <= nj < m and map_list[ni][nj] == 0:
                        sea += 1
                next_map[i][j] = max(0, map_list[i][j] - sea)
    return next_map

def bfs(start, visited, map_list, n, m):
    q = deque([start])
    visited[start[0]][start[1]] = True
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if map_list[nx][ny] > 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

def count_ice_chunks(map_list, n, m):
    visited = [[False] * m for _ in range(n)]
    chunk_count = 0
    for i in range(n):
        for j in range(m):
            if map_list[i][j] > 0 and not visited[i][j]:
                bfs((i, j), visited, map_list, n, m)
                chunk_count += 1
    return chunk_count

def simulate(map_list, n, m):
    year = 0
    while True:
        chunks = count_ice_chunks(map_list, n, m)
        if chunks >= 2:
            return year
        if chunks == 0:
            return 0
        map_list = melt(map_list, n, m)
        year += 1

n, m = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(n)]

result = simulate(map_list, n, m)
print(result)