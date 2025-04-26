N = int(input())
mtx = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N) :
    for j in range(N) :
        if i == N-1 and j == N - 1 :
            continue
        
        v = mtx[i][j]
        
        # right
        if j + v < N :
            newJ = j + v
            dp[i][newJ] += dp[i][j]

        # down
        if i + v < N :
            newI = i + v
            dp[newI][j] += dp[i][j]

# print(*dp, sep = '\n')
print(dp[N-1][N-1])