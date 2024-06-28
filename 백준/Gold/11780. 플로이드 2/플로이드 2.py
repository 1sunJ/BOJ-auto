import sys

INF = sys.maxsize
input = sys.stdin.readline

def makePath(i, j):
    k = pathMtx[i][j]
    if k == -1:
        return [i]
    return makePath(i,k) + makePath(k, j)

N, M = int(input()), int(input())
costs = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1) :
    costs[i][i] = 0

pathMtx = [[-1] * (N + 1) for _ in range(N + 1)]

for _ in range(M) :
    v1, v2, w = map(int, input().split())
    if w < costs[v1][v2] :
        costs[v1][v2] = w

for k in range(1, N + 1) :
    for i in range(1, N + 1) :
        for j in range(1, N + 1) :
            if costs[i][j] > costs[i][k] + costs[k][j] :
                costs[i][j] = costs[i][k] + costs[k][j]
                pathMtx[i][j] = k

for xx in costs[1::] :
    for x in xx[1::] :
        print(0 if x == INF else x, end = ' ')
    print()

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j or costs[i][j] == INF:
            print(0)
        else:
            l = makePath(i, j) + [j]
            print(len(l), *l)