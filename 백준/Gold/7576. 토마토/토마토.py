from collections import deque

MOVE = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs() :

    while que :
        x, y, t = que.popleft()

        for xx, yy in MOVE :
            xx, yy = xx + x, yy + y
            if not 0 <= xx < N or not 0 <= yy < M or mtx[xx][yy] :
                continue

            que.append([xx, yy, t+1])
            mtx[xx][yy] = t+1
        

M, N = map(int, input().split())
mtx = [list(map(int, input().split())) for _ in range(N)]

que = deque([])
for i in range(N) :
    for j in range(M) :
        if mtx[i][j] == 1 :
            que.append([i, j, 1])

bfs()

answer = 0
for x in mtx :
    for xx in x :
        if xx == 0 :
            answer = 0
            break
        answer = max(answer, xx)

    if answer == 0 :
        break

print(answer - 1)