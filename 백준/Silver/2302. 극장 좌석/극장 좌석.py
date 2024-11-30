N = int(input())
M = int(input())
s = set([int(input()) for _ in range(M)])

dp = [[0] * (N + 1) for _ in range(2)]
dp[0][1] = 1

for i in range(2, N + 1) :
    if i in s :
        dp[0][i] = dp[0][i - 1] + dp[1][i -1]
    else :
        if i - 1 in s :
            dp[0][i] = dp[0][i - 1]
        else :
            dp[0][i] = dp[0][i - 1] + dp[1][i - 1]
            dp[1][i] = dp[0][i - 1]

print(dp[0][N] + dp[1][N])