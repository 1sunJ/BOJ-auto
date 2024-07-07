from collections import deque

LENGTH_OF_SPACE = 500001

N, K = map(int, input().split())

visited = [[-1] * LENGTH_OF_SPACE for _ in range(2)] # visited[even/odd][point] = time
visited[0][N] = 0
que = deque([(N, 0)])

while que :
    x, t = que.popleft()
    y = K + int(t * (t+1) / 2)

    if x == y : # find answer 1
        print(t)
        exit()

    if visited[t%2][y] != -1 : # find answer 2
        print(t)
        exit()

    for mx in (x - 1, x + 1, x * 2) :
        if 0 <= mx < LENGTH_OF_SPACE and visited[(t+1)%2][mx] == -1 and y + (t+1) < LENGTH_OF_SPACE :
            que.append((mx, t + 1))
            visited[(t+1)%2][mx] = t + 1

print(-1)