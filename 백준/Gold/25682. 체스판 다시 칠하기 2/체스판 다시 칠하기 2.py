N, M, K = map(int, input().split())
mtx = [list(input()) for _ in range(N)]

cumulativeMtx = [[[0] * 2 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(N) :
    for j in range(M) :
        for k in range(2) :
            x = cumulativeMtx[i-1][j][k-1]
            y = cumulativeMtx[i][j-1][k-1]
            z = cumulativeMtx[i-1][j-1][k]
            cumulativeMtx[i][j][k] = x + y - z
        if mtx[i][j] == 'B' :
            cumulativeMtx[i][j][0] += 1

answer = N * M // 2
for i in range(K - 1, N) :
    for j in range(K - 1, M) :
        result = [0, 0]
        for k in range(2) :
            w = cumulativeMtx[i][j][k]
            x = cumulativeMtx[i-K][j][k-(K % 2)]
            y = cumulativeMtx[i][j-K][k-(K % 2)]
            z = cumulativeMtx[i-K][j-K][k]
            result[k] = w - x - y + z
        answer = min(answer, result[0] + ((K ** 2)//2 - result[1]), result[1] + ((K ** 2)//2 + K % 2 - result[0]))

print(answer)