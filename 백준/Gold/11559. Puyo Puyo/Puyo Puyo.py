from collections import deque

MOVE = ((-1, 0), (1, 0), (0, -1), (0, 1))
N, M = 12, 6

# find same color
# input point | output points
def bfs(i, j) :
    que = deque([(i, j)])

    points = [(i, j)]
    while que :
        x, y = que.popleft()
    
        for mx, my in MOVE :
            mx, my = mx + x, my + y
            if not 0 <= mx < N or not 0 <= my < M or visited[mx][my] or mtx[mx][my] != mtx[i][j] :
                continue

            que.append((mx, my))
            visited[mx][my] = True
            points.append((mx, my))
    
    return points

mtx = [list(input()) for _ in range(N)]

answer = 0
while True :
    isRemoved = False
    visited = [[False] * M for _ in range(N)]
    for i in range(N) :
        for j in range(M) :
            if visited[i][j] or mtx[i][j] == '.' :
                continue

            # BFS 탐색
            visited[i][j] = True
            points = bfs(i, j)

            # 뿌요 파괴
            if len(points) >= 4 :
                for x, y in points :
                    mtx[x][y] = '.'
                isRemoved = True

    # 뿌요 재배치
    for j in range(M) :
        isRearranged = True
        while isRearranged :
            isRearranged = False
            # 가장 아래 빈 공간 찾기
            bottomEmpty = 0
            for i in range(N-1, -1, -1) :
                if mtx[i][j] == '.' :
                    bottomEmpty = i
                    break

            # 가장 아래 뿌요 찾기
            bottomPuyo = -1
            for i in range(bottomEmpty - 1, -1, -1) :
                if mtx[i][j] != '.' :
                    bottomPuyo = i
                    break
            
            if bottomPuyo != - 1 :
                mtx[bottomPuyo][j], mtx[bottomEmpty][j] = mtx[bottomEmpty][j], mtx[bottomPuyo][j]
                isRearranged = True

    if isRemoved :
        answer += 1
    else :
        break

print(answer)