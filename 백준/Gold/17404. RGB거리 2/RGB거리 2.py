import sys
INF = sys.maxsize

N = int(input())
mtx = [list(map(int, input().split())) for _ in range(N)]

answer = INF
for i in range(3) :
    dp = [[INF, INF, INF] for _ in range(N)]
    dp[0][i] = mtx[0][i]

    for j in range(1, N) :
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + mtx[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + mtx[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + mtx[j][2]

    for j in range(3) :
        if i != j :
            answer = min(answer, dp[-1][j])

print(answer)