from collections import deque
MOVE = ((-1, 0), (1, 0), (0, -1), (0, 1))

N, M = map(int, input().split())
mtx = [list(input()) for _ in range(N)]

# 고슴 S / 비버굴 E / 물 * / 돌 X
wPoints = []
rPoints = []
for i in range(N) :
    for j in range(M) :
        if mtx[i][j] == 'S' :
            S = (i, j)
        if mtx[i][j] == 'D' :
            E = (i, j)
        if mtx[i][j] == '*' :
            wPoints.append((i, j))
        if mtx[i][j] == 'X' :
            rPoints.append((i, j))

visited = [[0] * M for _ in range(N)]
que = deque([])

que.append([S[0], S[1]])
visited[S[0]][S[1]] = 1

for x, y in wPoints :
    que.append([x, y])
    visited[x][y] = -1

while que :
    x, y = que.popleft()
    # print("\nx, y", x, y)

    if mtx[x][y] == '*' :
        for xx, yy in MOVE :
            xx, yy = x+xx, y+yy
            if not 0 <= xx < N or not 0 <= yy < M or mtx[xx][yy] == '*' or mtx[xx][yy] == 'X' or mtx[xx][yy] == 'D' :
                continue
            
            que.append([xx, yy])
            visited[xx][yy] = -1
            mtx[xx][yy] = '*'
    else :
        for xx, yy in MOVE :
            xx, yy = x+xx, y+yy
            if not 0 <= xx < N or not 0 <= yy < M :
                continue

            if mtx[xx][yy] == 'D' :
                print(visited[x][y])
                exit()

            if mtx[xx][yy] != '.' or visited[xx][yy] :
                continue
            
            que.append([xx, yy])
            visited[xx][yy] = visited[x][y] + 1

    # printt()
    
print('KAKTUS')