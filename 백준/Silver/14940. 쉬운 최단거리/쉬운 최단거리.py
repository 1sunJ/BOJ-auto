from collections import deque
MOVE = [[-1, 0], [1, 0], [0, -1], [0, 1]]

N, M = map(int, input().split())
mtx = [list(map(int, input().split())) for _ in range(N)]
for i in range(N) :
    for j in range(M) :
        if mtx[i][j] == 2 :
            px, py = i, j

que = deque([[px, py]])
visited = [[0] * M for _ in range(N)]
visited[px][py] = 1

while que :
    x, y = que.popleft()

    for xx, yy in MOVE :
        xx, yy = x + xx, y + yy
        if not 0 <= xx < N or not 0 <= yy < M :
            continue

        if not visited[xx][yy] and mtx[xx][yy] :
            que.append([xx, yy])
            visited[xx][yy] = visited[x][y] + 1

for i in range(N) :
    for j in range(M) :
        if visited[i][j] :
            visited[i][j] -= 1
        else :
            if mtx[i][j] :
                visited[i][j] = -1

for x in visited :
    print(*x)