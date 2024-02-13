# MOVE = [[0, 1], [1, 0], [0, -1], [-1, 0]]
MOVE = [[0, 1], [1, 0]]

N, M = map(int, input().split())
mtx = [list(input()) for _ in range(N)]
answer = 0

j = 0
len = 0
while j < M :
    if mtx[0][j] == '.' :
        j += 1
        len += 1
    else :
        j += 1
        answer += len // 2
        len = 0

    answer += len // 2

for i in range(1, N) :
    j = 0
    len = 0
    while j < M :
        if mtx[i][j] == '.' and mtx[i-1][j] == 'X' :
            j += 1
            len += 1
        else :
            j += 1
            answer += len // 2
            len = 0
    
    answer += len // 2

j = 0
len = 0
while j < M :
    if mtx[N-1][j] == '.' :
        j += 1
        len += 1
    else :
        j += 1
        answer += len // 2
        len = 0

    answer += len // 2

for i in range(0, N-1) :
    j = 0
    len = 0
    while j < M :
        if mtx[i][j] == '.' and mtx[i+1][j] == 'X' :
            j += 1
            len += 1
        else :
            j += 1
            answer += len // 2
            len = 0
    
    answer += len // 2


# 세로
j = 0
len = 0
while j < N :
    if mtx[j][0] == '.' :
        j += 1
        len += 1
    else :
        j += 1
        answer += len // 2
        len = 0

    answer += len // 2 

for i in range(1, M) :
    j = 0
    len = 0
    while j < N :
        if mtx[j][i] == '.' and mtx[j][i-1] == 'X' :
            j += 1
            len += 1
        else :
            j += 1
            answer += len // 2
            len = 0

    answer += len // 2 

j = 0
len = 0
while j < N :
    if mtx[j][M-1] == '.' :
        j += 1
        len += 1
    else :
        j += 1
        answer += len // 2
        len = 0

    answer += len // 2 

for i in range(0, M-1) :
    j = 0
    len = 0
    while j < N :
        if mtx[j][i] == '.' and mtx[j][i+1] == 'X' :
            j += 1
            len += 1
        else :
            j += 1
            answer += len // 2
            len = 0

    answer += len // 2 


print(answer)