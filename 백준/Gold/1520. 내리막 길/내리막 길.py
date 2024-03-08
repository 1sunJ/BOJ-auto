import sys
sys.setrecursionlimit(10**6)

MOVE = ((-1, 0), (1, 0), (0, -1), (0, 1))

def dfs(x, y) :
    if (x, y) == (N-1, M-1) :
        return 1
    
    if dp[x][y] != -1 :
        return dp[x][y]

    ways = 0
    for i, j in MOVE :
        i, j = i+x, j+y

        if not 0 <= i < N or not 0 <= j < M :
            continue

        if mtx[x][y] > mtx[i][j]:
            ways += dfs(i, j)

    dp[x][y] = ways

    return dp[x][y]


N, M = map(int, input().split())
mtx = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * M for _ in range(N)]

print(dfs(0, 0))
# print('--------------')
# print(*dp, sep = '\n')
# print('--------------')