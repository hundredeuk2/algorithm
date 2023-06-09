n = int(input())
num_list = list(map(int, input().split()))

dp = [num_list[0], max(num_list[0]*2, num_list[1])]
for i in range(2,n):
    if i % 2 == 0:
        dp_f = dp[:i//2]
        dp_b = dp[i//2:]
        M = 0
        for j in range(i//2):
            M = max(M, dp_f[j]+dp_b[-(j+1)])
        dp.append(max(M, num_list[i]))
        
    else:
        dp_f = dp[:i//2]
        dp_b = dp[i//2+1:]
        M = dp[i//2] * 2
        for j in range(i//2):
            M = max(M, dp_f[j]+dp_b[-(j+1)])
        dp.append(max(M, num_list[i]))

print(dp[-1])