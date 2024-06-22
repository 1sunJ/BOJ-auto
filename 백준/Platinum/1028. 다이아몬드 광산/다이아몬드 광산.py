N, M = map(int, input().split())
mtx = [[0] * (M + 1)] + [[0] + list(map(int, input())) for _ in range(N)]

# print(*mtx, sep = '\n')

diaMtx = [[[0, 0] for _ in range(M + 2)] for _ in range(N + 2)]

for i in range(1, N + 1) :
    for j in range(1, M + 1) :
        diaMtx[i][j][0] = diaMtx[i-1][j-1][0] * mtx[i][j] + mtx[i][j]
        diaMtx[i][j][1] = diaMtx[i-1][j+1][1] * mtx[i][j] + mtx[i][j]

# print(*diaMtx, sep = '\n')

check = True
for x in mtx :
    for xx in x :
        if xx :
            check = False
if check : 
    print(0)
    exit()

answer = 1
for i in range(1, N + 1) :
    for j in range(1, M + 1) :
        # bottom / left / right
        bottom = min(diaMtx[i][j])
        for s in range(bottom, answer, -1) :
            left = diaMtx[i-(s-1)][j-(s-1)][1]
            right = diaMtx[i-(s-1)][j+(s-1)][0]

            if s <= left and s <= right :
                answer = s
                break

print(answer)