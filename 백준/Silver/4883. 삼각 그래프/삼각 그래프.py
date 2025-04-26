# 음수 가능인지는 몰랐지 !!!!

import sys
MAX= sys.maxsize
input = sys.stdin.readline

MOVES = ((0, 1), (1, 1), (1, -1), (1, 0))

t = 1
while True :
    N = int(input())
    if N == 0 :
        break

    mtx = [list(map(int, input().split())) for _ in range(N)]
    dp = [[MAX] * 3 for _ in range(N)]
    
    dp[0] = mtx[0][::]
    dp[0][2] = mtx[0][1] + mtx[0][2]
    dp[1][0] = dp[0][1] + mtx[1][0]
    dp[1][1] = min(dp[0][1], dp[0][2], dp[1][0]) + mtx[1][1]
    dp[1][2] = min(dp[0][1], dp[0][2], dp[1][1]) + mtx[1][2]

    for i in range(1, N) :
        for j in range(3) :
            for mx, my in MOVES :
                x, y = i + mx, j + my
                if not 0 <= x < N or not 0 <= y < 3 :
                    continue

                dp[x][y] = min(dp[x][y], dp[i][j] + mtx[x][y])

    # print(*dp, sep = '\n')

    print("%d. %d" %(t, dp[N-1][1]))
    t += 1