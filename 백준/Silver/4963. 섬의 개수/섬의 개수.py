MOVE = ((0, -1), (-1, -1), (-1, 0), (-1, 1)
        , (0, 1), (1, 1), (1, 0), (1, -1))

from collections import deque

while True :
    M, N = map(int, input().split())
    if not N and not M :
        break

    mtx = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * M for _ in range(N)]

    result = 0
    for i in range(N) :
        for j in range(M) :
            if visited[i][j] or mtx[i][j] == 0:
                continue

            result += 1
            visited[i][j] = True
            que = deque([(i, j)])

            while que :
                x, y = que.popleft()

                for mx, my in MOVE :
                    mx, my = mx + x, my + y
                    if not 0 <= mx < N or not 0 <= my < M or visited[mx][my] or mtx[mx][my] == 0 :
                        continue

                    que.append((mx, my))
                    visited[mx][my] = True

    print(result)