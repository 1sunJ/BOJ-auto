from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
adjList = [[] for _ in range(N+1)]
for i in range(M) :
    a, b = map(int, input().split())
    adjList[a].append(b)

visited = [False] * (N+1)
visited[X] = 1
que = deque([X])

while que :
    x = que.popleft()
    if visited[x] > K+1 :
        continue

    for y in adjList[x] :
        if visited[y] :
            continue

        visited[y] = visited[x] + 1
        que.append(y)

# print("visited", visited)

existFlag = False
for i in range(1, N+1) :
    if visited[i] == K+1 :
        print(i)
        existFlag = True

if not existFlag :
    print(-1)