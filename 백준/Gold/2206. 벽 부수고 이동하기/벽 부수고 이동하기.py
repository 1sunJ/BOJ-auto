from collections import deque
MOVE = ((-1, 0), (1, 0), (0, -1), (0, 1))

N, M = map(int, input().split())
K = 1
mtx = [list(map(int, input())) for _ in range(N)]

visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

que = deque([(0, 0, 0)])

while que :
    x, y, z = que.popleft()
    # print('x, y, z', x, y, z)

    findAnswer = False
    for v in visited[N-1][M-1] :
        if v :
            findAnswer = True
            break
    if findAnswer :
        # print("!! FIND !!")
        break

    for xx, yy in MOVE :
        xx, yy = x + xx, y + yy
        if not 0 <= xx < N or not 0 <= yy < M :
            continue
        
        # to 길
        if mtx[xx][yy] == 0 :
            if not visited[xx][yy][z] :
                visited[xx][yy][z] = visited[x][y][z] + 1
                que.append((xx, yy, z))

        # to 벽
        else :
            if z < K and not visited[xx][yy][z+1]:
                visited[xx][yy][z+1] = visited[x][y][z] + 1
                que.append((xx, yy, z+1))

    # print("==================")
    # for v in visited :
    #     print(v)

for x in visited[N-1][M-1] :
    if x :
        print(x)
        exit()

print(-1)