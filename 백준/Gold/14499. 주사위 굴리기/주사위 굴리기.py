MOVE = [None, [0, 1], [0, -1], [-1, 0], [1, 0]]

#  d : 1 = 동 | 2 = 서 | 3 = 북 | 4 = 남
def move(d) :
    global dice1, dice2

    if d < 3 :
        if d == 1 :
            dice1 = dice1[1::] + [dice1[0]]
        else :
            dice1 = [dice1[-1]] + dice1[:3:]

        dice2[0], dice2[2] = dice1[0], dice1[2]
    
    else :
        if d == 3 :
            dice2 = [dice2[-1]] + dice2[:3:]
        else :
            dice2 = dice2[1::] + [dice2[0]]

        dice1[0], dice1[2] = dice2[0], dice2[2]

N, M, x, y, K = map(int, input().split())
mtx = [list(map(int, input().split())) for _ in range(N)]
moves = list(map(int, input().split()))

dice1 = [0] * 4 # 가로 : 상 왼 하 우
dice2 = [0] * 4 # 세로 : 상 위 하 아

for d in moves :
    x, y = x + MOVE[d][0], y + MOVE[d][1]

    if not 0 <= x < N or not 0 <= y < M :
        x, y = x - MOVE[d][0], y - MOVE[d][1]
        continue

    move(d)

    if mtx[x][y] == 0 :
        mtx[x][y] = dice1[2]
    else :
        dice1[2] = dice2[2] = mtx[x][y]
        mtx[x][y] = 0

    print(dice1[0])