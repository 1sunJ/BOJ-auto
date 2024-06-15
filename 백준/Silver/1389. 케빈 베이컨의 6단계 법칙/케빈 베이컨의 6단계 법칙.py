import sys
from collections import deque

INF = sys.maxsize

N, M = map(int, input().split())
adjList = [[] for _ in range(N+1)]
for _ in range(M) :
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

answer = [1, INF]
for i in range(1, N + 1) :

    visited = [-1] * (N+1)
    visited[i] = 0
    que = deque([i])

    while que : 
        x = que.popleft()

        for adj in adjList[x] :
            if visited[adj] != -1 :
                continue

            que.append(adj)
            visited[adj] = visited[x] + 1

    result = sum(visited)
    if answer[1] > result :
        answer = [i, result]

print(answer[0])