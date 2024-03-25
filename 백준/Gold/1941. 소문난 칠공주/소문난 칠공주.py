from collections import deque
MOVE = ((-1, 0), (1, 0), (0, -1), (0, 1))

# bfs
def isConnected() :
    visited = [[0] * (N+1) for _ in range(N+1)]
    for x, y in points :
        visited[x][y] = 1
    visited[points[0][0]][points[0][1]] = 2
    
    que = deque([])
    que.append([points[0][0], points[0][1]])
    l = 1

    while que :
        x, y = que.popleft()
        for xx, yy in MOVE :
            xx, yy = x+xx, y+yy
            if not 1 <= xx <= N or not 1 <= yy <= N or visited[xx][yy] != 1 :
                continue

            que.append([xx, yy])
            visited[xx][yy] = 2
            l += 1

    return True if l == 7 else False

def dfs(idx, so, ye) :
    if ye == 4 :
        return
    
    if so + ye == 7 :
        if isConnected() :
            global answer
            answer += 1
        return
    
    for i in range(idx, N ** 2) :
        x, y = idxs[i]
        points.append([x, y])
        dfs(i + 1,
            so + 1 if mtx[x][y] == 'S' else so,
            ye + 1 if mtx[x][y] == 'Y' else ye
            )
        points.pop()

N = 5
mtx = [[]] + [[0] + list(input()) for _ in range(N)]

idxs = []
for i in range(1, N+1) :
    for j in range(1, N+1) :
        idxs.append([i, j])

answer = 0
points = []
dfs(0, 0, 0)

print(answer)