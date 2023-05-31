t = int(input())
num_list = []
for _ in range(t):
    num_list.append(int(input()))
    
dp = [1,1,1]
for i in range(2, max(num_list)):
    tmp = dp[i-2] + dp[i-1]
    dp.append(tmp)

for num in num_list:
    print(dp[num-1])