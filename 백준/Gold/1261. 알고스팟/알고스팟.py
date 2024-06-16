from collections import deque
import sys
input = sys.stdin.readline

# input
M, N = map(int, input().split())
arr = [list(map(int, *input().split())) for _ in range(N)]

# BFS
move = [[-1,0], [1,0], [0,-1], [0,1]]
que = deque([[0,0]])
visited = [[0]*M for _ in range(N)] # record number of times breaking a wall
visited[0][0] = 1

while que :
    x, y = que.popleft()

    for i, j in move : 
        i, j = i+x, j+y
        if 0 <= i < N and 0 <= j < M :
            if not visited[i][j] :
                if arr[i][j] :  # wall
                    que.append([i, j])
                    visited[i][j] = visited[x][y] + 1
                else :  # empty room
                    que.appendleft([i, j])
                    visited[i][j] = visited[x][y]

print(visited[N-1][M-1] - 1)