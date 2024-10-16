from collections import deque

MOVE = ((-1, 0), (0, -1), (0, 1), (1, 0))

# return newX, newY, t
def find() :
    fishes = []
    tt = 0

    visited = [[0] * N for _ in range(N)]
    que = deque([(x, y)])
    visited[x][y] = 1

    while que :
        xx, yy = que.popleft()

        if mtx[xx][yy] and mtx[xx][yy] < level :
            if tt == 0 :
                tt = visited[xx][yy] - 1
            elif visited[xx][yy] - 1 > tt :
                break
            fishes.append([xx, yy])
        
        for mx, my in MOVE :
            mx, my = mx + xx, my + yy
            if not 0 <= mx < N or not 0 <= my < N or visited[mx][my] :
                continue

            if mtx[mx][my] <= level :
                visited[mx][my] = visited[xx][yy] + 1
                que.append((mx, my))

    if tt :
        fishes.sort(key=lambda x : (x[0], x[1]))
        xx, yy = fishes[0]
        return [xx] + [yy] + [visited[xx][yy] - 1]

    return None

N = int(input())
mtx = [list(map(int, input().split())) for _ in range(N)]

x, y = -1, -1 # 상어의 현재 위치
for i in range(N) :
    for j in range(N) :
        if mtx[i][j] == 9 :
            mtx[i][j] = 0
            x, y = i, j
            break
    if x != -1 : break

level = 2
exp = 0 # if level == exp : level += 1, exp = 0
t = 0

while True :
    result = find()
    if not result :
        break

    x, y, t = result[0], result[1], t + result[2]
    mtx[x][y] = 0
    exp += 1
    if level == exp :
        level += 1
        exp = 0

print(t)