n = int(input())
coord = []
for _ in range(n):
    tmp = list(map(int, input().split()))  # n * 3 : list[int]
    coord.append(tmp)
    
dp = [[0 for _ in range(3)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(3):
        m = int(1e15)
        for k in range(3):
            if k ==j:
                continue
            m = min(m, dp[i-1][k])
        dp[i][j] = coord[i-1][j] + m
print(min(dp[-1]))