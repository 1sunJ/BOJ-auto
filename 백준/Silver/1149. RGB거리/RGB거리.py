import sys
input = sys.stdin.readline
NUMBER_OF_COLORS = 3

# input : N / lists
N = int(input())
mtx = [list(map(int, input().split())) for _ in range(N)]

# dp table : i 번째가 x 컬러일 때 최소 비용 (x -> R G B)
dp = [[0] * NUMBER_OF_COLORS for _ in range(N)]

# make dp table
for i in range(N) :
    for j in range(NUMBER_OF_COLORS) :
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j-2]) + mtx[i][j]

# output : the answer
print(min(dp[N-1]))

# test print
# print(*dp, sep = '\n')