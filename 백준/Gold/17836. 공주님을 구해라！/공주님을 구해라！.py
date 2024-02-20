from collections import deque
MOVE = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M, T = map(int, input().split())
mtx = [list(map(int, input().split())) for _ in range(N)]

# find gram
gram = 0
for i in range(N) :
    for j in range(M) :
        if mtx[i][j] == 2 :
            gram = (i, j)
        if gram :
            break
    if gram :
        break

que = deque([[0, 0]])
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

while que :
    i, j = que.popleft()

    # # fail
    # if visited[i][j] > T + 1 :
    #     break

    for x, y in MOVE :
        x, y = x+i, y+j

        if not 0 <= x < N or not 0 <= y < M or mtx[x][y] == 1  or visited[x][y] :
            continue

        visited[x][y] = visited[i][j] + 1
        que.append([x, y])

# print("visited")
# for x in visited :
#     print(*x)


answer = visited[N-1][M-1]
x, y = gram
gramTime = visited[x][y] + N-x-1 + M-y-1

if answer and not visited[x][y] :
    pass
elif answer and visited[x][y] :
    answer = min(answer, gramTime)
elif visited[x][y] :
    answer = gramTime
else :
    answer = 0
answer -= 1

if answer > T :
    answer = -1

    # print("!!", answer)
    # print("!!", gramTime, visited[x][y], x, y)


if answer == -1 :
    print("Fail")
else :
    print(answer)