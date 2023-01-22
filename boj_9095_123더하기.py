n = int(input())

def dyn(num):
    dp = [1,2,4]
    for i in range(3,num+1):
        dp.append(dp[i-3]+ dp[i-2]+dp[i-1])
    return print(dp[num-1])

for _ in range(n):
    number = int(input())
    dyn(number)
