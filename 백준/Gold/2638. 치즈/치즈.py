from collections import deque

MOVE = ((-1, 0), (1, 0), (0, -1), (0, 1))

N, M = map(int, input().split())
mtx = [list(map(int, input().split())) for _ in range(N)]

cheeseList = []
for i in range(N) :
    for j in range(M) :
        if mtx[i][j] :
            cheeseList.append((i, j))

t = 0
while True :
    if not cheeseList :
        break

    t += 1

    cheeseStack = dict()
    for x, y in cheeseList :
        cheeseStack[(x, y)] = 0

    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    que = deque([(0, 0)])

    while que :
        x, y = que.popleft()

        for mx, my in MOVE :
            mx, my = mx + x, my + y
            if not 0 <= mx < N or not 0 <= my < M or visited[mx][my] :
                continue

            if mtx[mx][my] :
                cheeseStack[(mx, my)] += 1
            else :
                que.append((mx, my))
                visited[mx][my] = True

    for x, y in cheeseStack :
        if cheeseStack[(x, y)] >= 2 :
            cheeseList.remove((x, y))
            mtx[x][y] = 0

    # print("!!!", t)
    # for x in mtx :
    #     print(*x, sep = ' ')

print(t)