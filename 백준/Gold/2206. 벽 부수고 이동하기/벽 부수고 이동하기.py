from collections import deque
import sys

input = sys.stdin.readline
MOVE = [[-1, 0], [1, 0], [0, -1], [0, 1]]

N, M = map(int, input().split())
mtx = [list(map(int, input().rstrip())) for _ in range(N)]

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
visited[0][0][1] = 1
que = deque([])
que.append([0, 0])

# t = 150
while que :
    x, y = que.popleft()
    # print("!!", x, y, que)

    for xx, yy in MOVE :
        xx, yy = x + xx, y + yy

        if not 0 <= xx < N or not 0 <= yy < M or (visited[xx][yy][0] and visited[xx][yy][1]) :
            continue

        if visited[x][y][0] and not visited[xx][yy][0] and visited[xx][yy][1] :
            if not mtx[xx][yy] :
                visited[xx][yy][0] = visited[x][y][0] + 1
                que.append([xx, yy])
                continue

        if not visited[xx][yy][0] and not visited[xx][yy][1] :
            # 벽인 경우
            if mtx[xx][yy] :
                # 갈 수 있음
                if visited[x][y][0] :
                    visited[xx][yy][1] = visited[x][y][0] + 1
                    que.append([xx, yy])

            # 아닌 경우
            else :
                if visited[x][y][0] :
                    visited[xx][yy][0] = visited[x][y][0] + 1
                
                if visited[x][y][1] :
                    visited[xx][yy][1] = visited[x][y][1] + 1
                else :
                    visited[xx][yy][1] = visited[xx][yy][0]

                if visited[xx][yy][0] or visited[xx][yy][1] :
                    que.append([xx, yy])

    # print(*visited, sep='\n')
    # print("==============")
    # t -= 1
    # if not t : break

if visited[N-1][M-1][0] == 0 and visited[N-1][M-1][1] == 0 :
    print(-1)
else :
    if visited[N-1][M-1][0] == -1 or visited[N-1][M-1][0] == 0 :
        print(visited[N-1][M-1][1])
    elif visited[N-1][M-1][1] == -1 or visited[N-1][M-1][1] == 0 :
        print(visited[N-1][M-1][0])
    else :
        print(min(visited[N-1][M-1]))