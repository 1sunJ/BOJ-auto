MOVE = ((-1, -1), (-1, 1), (1, -1), (1, 1))

def btrk(idxs, idx, cnt) :
    if idx == len(idxs) - 1 :
        global result
        result = max(result, cnt)
        return
    
    x, y = idxs[idx + 1]
    if not visited[0][x + y] and not visited[1][x - y] :
        visited[0][x + y] = True # 좌하향 대각선
        visited[1][x - y] = True # 우하향 대각선
        btrk(idxs, idx + 1, cnt + 1)
        visited[0][x + y] = False
        visited[1][x - y] = False

    btrk(idxs, idx + 1, cnt)


N = int(input())
mtx = [[]] + [[0] + list(map(int, input().split())) for _ in range(N)]

idxs1 = [] # white
idxs2 = []
w = True
for i in range(1, N + 1) :
    for j in range(1, N + 1) :
        if mtx[i][j] :
            idxs1.append((i, j)) if w else idxs2.append((i, j))
        w = bool(int(w) - 1)
    if N % 2 == 0 :
        w = bool(int(w) - 1)

visited = [[False] * (N * 3) for _ in range(2)] # 쉽게 충돌여부 확인하기

answer = 0
result = 0
btrk(idxs1, -1, 0)

answer += result
result = 0
btrk(idxs2, -1, 0)

print(answer + result)