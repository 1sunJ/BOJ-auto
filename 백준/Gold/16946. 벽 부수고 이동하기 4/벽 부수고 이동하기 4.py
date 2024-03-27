from collections import deque
MOVE = ((-1, 0), (1, 0), (0, -1), (0, 1))

N, M = map(int, input().split())
mtx = [list(map(int, input())) for _ in range(N)]

area = [0]

visited = [[0] * M for _ in range(N)]
que = deque([])

for i in range(N) :
    for j in range(M) :
        if mtx[i][j] or visited[i][j] :
            continue

        cnt = 0
        areaN = len(area)
        visited[i][j] = areaN
        que.append([i, j])

        while que :
            x, y = que.popleft()
            cnt += 1

            for xx, yy in MOVE :
                xx, yy = x + xx, y + yy
                if not 0 <= xx < N or not 0 <= yy < M or mtx[xx][yy] or visited[xx][yy] :
                    continue

                que.append([xx, yy])
                visited[xx][yy] = areaN

        area.append(cnt)

# print('=========')
# print(area)
# for x in visited :
#     print(x)
# print('=========')

answer = [[0] * M for _ in range(N)]
for i in range(N) :
    for j in range(M) :
        if not mtx[i][j] :
            continue

        answer[i][j] += 1
        areaSet = set()
        for x, y in MOVE :
            x, y = x + i, y + j
            if not 0 <= x < N or not 0 <= y < M or visited[x][y] in areaSet :
                continue

            answer[i][j] += area[visited[x][y]]
            areaSet.add(visited[x][y])
        
        answer[i][j] %= 10

for x in answer :
    print(*x, sep = '')