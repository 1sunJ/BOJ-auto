from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
adjList = [[] for _ in range(N+1)]
for _ in range(N - 1) :
    v1, v2 = map(int, input().split())
    adjList[v1].append(v2)
    adjList[v2].append(v1)

roots = [1] * (N + 1)

que = deque([1])
visited = [0] * (N + 1)
visited[1] = True

while que :
    x = que.popleft()

    for adj in adjList[x] :
        if not visited[adj] :
            que.append(adj)
            visited[adj] = True
            roots[adj] = x

print(*roots[2::], sep = '\n')