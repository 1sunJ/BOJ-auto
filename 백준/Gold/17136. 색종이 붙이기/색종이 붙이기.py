import sys
sys.setrecursionlimit(10**6)

N = 10
SIZE = (5, 4, 3, 2, 1)

def check(x, y, size) :
    if not 0 <= x + size <= N or not 0 <= y + size <= N or counts[size] == 0 :
        return False
    
    for i in range(x, x + size) :
        for j in range(y, y + size) :
            if mtx[i][j] == 0 :
                return False
            
    return True

def cover(x, y, size) :
    counts[size] -= 1

    for i in range(x, x+size) :
        for j in range(y, y+size) :
            mtx[i][j] = 0

def recover(x, y, size) :
    counts[size] += 1

    for i in range(x, x+size) :
        for j in range(y, y+size) :
            mtx[i][j] = 1

limit = 0

def dfs(ll, cnt) :
    if ll == l :
        global answer
        answer = min(answer, cnt)
        return
    
    i, j = points[ll]

    if mtx[i][j] == 0 :
        dfs(ll + 1, cnt)

    # print("!!!", i, j)
    # print(*mtx, sep = '\n')
    
    for s in SIZE :
        if not check(i, j, s) :
            continue
        
        cover(i, j, s)
        dfs(ll + 1, cnt+1)
        recover(i, j, s)


mtx = [list(map(int, input().split())) for _ in range(N)]
counts = {i : 5 for i in range(1, 6)}
points = []
for i in range(N) :
    for j in range(N) :
        if mtx[i][j] == 1 :
            points.append([i, j])
l = len(points)

answer = 26
dfs(0, 0)
if answer == 26 :
    print(-1)
else :
    print(answer)