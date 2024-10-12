import sys
sys.setrecursionlimit(10 ** 6)

MOVE = ((0, -1), (-1, 0), (0, 1), (1, 0))

def dfs(p) :
    x, y = p

    maxCnt = 1
    for mx, my in MOVE :
        mx, my = mx + x, my + y
        if not 0 <= mx < N or not 0 <= my < N or mtx[x][y] >= mtx[mx][my] :
            continue
        
        if not visited[mx][my] :
            dfs((mx, my))
        maxCnt = max(maxCnt, visited[mx][my] + 1)

    visited[x][y] = maxCnt

N = int(input())
mtx = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)] # value : (i, j) 에서 시작해서 거칠 수 있는 최대 포인트 개수

for i in range(N) :
    for j in range(N) :
        if visited[i][j] :
            continue

        dfs((i, j))

print(max(map(max, visited)))