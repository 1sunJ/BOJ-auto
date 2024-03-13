def calculateResult() :
    for i in range(N) :
        x, y = 0, i

        while x < H :
            if mtx[x][y] == 1 :
                y += 1
            elif mtx[x][y] == 2 :
                y -= 1

            x += 1
        
        if i != y :
            return False
        
    return True

def dfs(ll, cnt) :
    global answer
    # ???
    if cnt > 3 or cnt > answer :
        return
    
    if ll == l :
        if calculateResult() :
            answer = min(answer, cnt)
        return 
    
    h, n = points[ll]

    if not mtx[h][n] and not mtx[h][n+1] :
        mtx[h][n] = 1
        mtx[h][n+1] = 2
        if ll+1 < ll :
            hh, nn = points[ll+1]
            if h == hh and n +1 == nn :
                dfs(ll + 2, cnt + 1)
            else :
                dfs(ll + 1, cnt + 1)
        else :
            dfs(ll + 1, cnt + 1)
        mtx[h][n] = 0
        mtx[h][n+1] = 0

    dfs(ll + 1, cnt)

N, M, H = map(int, input().split())
mtx = [[0] * N for _ in range(H)]
for _ in range(M) :
    a, b = map(int, input().split())
    mtx[a-1][b-1] = 1 # 우향
    mtx[a-1][b] = 2 # 좌향

points = []
for i in range(H) :
    for j in range(N-1) :
        if not mtx[i][j] and not mtx[i][j+1] :
            points.append([i, j])
l = len(points)

answer = H * N + 1
dfs(0, 0)
if answer == H * N + 1 :
    print(-1)
else :
    print(answer)