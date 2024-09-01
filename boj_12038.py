MOD = 1000000007

def count_valid_words(C, V, L):
    dp = [[0 for _ in range(2)] for _ in range(L + 1)]
    
    # 초기 조건 설정
    dp[1][0] = V  
    
    # DP 테이블 채우기
    for i in range(2, L + 1):
        dp[i][0] = V * (dp[i-1][0] + dp[i-1][1]) % MOD
        dp[i][1] = C * dp[i-1][0] % MOD
    return dp[L][0]

def solve():
    T = int(input().strip())
    for t in range(1, T + 1):
        C, V, L = map(int, input().strip().split())
        result = count_valid_words(C, V, L)
        print(f"Case #{t}: {result}")

solve()