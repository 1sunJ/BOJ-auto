import sys
from collections import deque
input = sys.stdin.readline

DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
moves = deque([]) # sorting ?
for i in range(L) :
    a, b = input().split()
    moves.append([int(a), b])

x, y = 0, 0 # head
body = deque([[0, 0]])
dr = 0 # direction

mtx = [[0] * N for _ in range(N)]
mtx[0][0] = 1 # body
for i, j in apples :
    mtx[i-1][j-1] = 2 # apple

time = 0
while True :
    # print("%ds" %time)
    # for xx in mtx :
    #     print(*xx)
    # print()

    time += 1

    # move head
    dx, dy = DIRECTIONS[dr]
    x, y = x + dx, y + dy
    body.append([x, y])
    if not 0 <= x < N or not 0 <= y < N or mtx[x][y] == 1 :
        break

    # direction
    if moves :
        mt, md = moves[0]
        if mt == time :
            moves.popleft()
            if md == "D" :
                dr = (dr+1) % 4
            else :
                dr = (dr-1) % 4

    # apple ?
    if mtx[x][y] == 2 :
        mtx[x][y] = 1
        continue
    
    # no apple
    bx, by = body.popleft()
    mtx[bx][by] = 0

    mtx[x][y] = 1

print(time)