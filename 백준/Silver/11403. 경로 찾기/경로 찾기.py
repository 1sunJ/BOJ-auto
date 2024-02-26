from collections import deque

N = int(input())
adjMtx = [list(map(int, input().split())) for _ in range(N)]

answer = [[0] * N for _ in range(N)]

for i in range(N) :
    visited = [False] * N
    que = deque([i])

    while que :
        x = que.popleft()

        for j in range(N) :
            if visited[j] or adjMtx[x][j] == 0 :
                continue

            visited[j] = True
            que.append(j)
            answer[i][j] = 1

for x in answer :
    print(*x)