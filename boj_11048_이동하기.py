n, m = map(int, input().split())
coord = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    coord.append(tmp)
    
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + coord[i-1][j-1]
print(dp[n][m])