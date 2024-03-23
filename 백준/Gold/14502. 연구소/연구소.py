from itertools import combinations
from collections import deque
MOVE = ((-1, 0), (1, 0), (0, -1), (0, 1))

def bfs() :
    while que :
        x, y = que.popleft()

        for xx, yy in MOVE :
            xx, yy = x+xx, y+yy

            if not 0 <= xx < N or not 0 <= yy < M or mtx[xx][yy] != 0 or visited[xx][yy] :
                continue

            que.append([xx, yy])
            visited[xx][yy] = 1


N, M = map(int, input().split())
mtx = [list(map(int, input().split())) for _ in range(N)]

points = []
vPoints = []
for i in range(N) :
    for j in range(M) :
        if mtx[i][j] == 0 :
            points.append([i, j])
        if mtx[i][j] == 2 :
            vPoints.append([i, j])

combs = list(combinations(points, 3))
answer = 0

for comb in combs :
    for x, y in comb :
        mtx[x][y] = 1

    result = 0
    visited = [[0] * M for _ in range(N)]
    que = deque([])
    for vx, vy in vPoints :
        visited[vx][vy] = 1
        que.append([vx, vy])
    
    bfs()

    for i in range(N) :
        for j in range(M) :
            if mtx[i][j] == 0 and not visited[i][j]:
                result += 1

    answer = max(answer, result)
    # if answer < result :
    #     answer = result
    #     print(result)
    #     print(comb)
    #     for x in mtx :
    #         print(*x)
    #     print()
    #     for x in visited :
    #         print(*x)
    
    for x, y in comb :
        mtx[x][y] = 0
    
print(answer)