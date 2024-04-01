from collections import deque

N, M = map(int, input().split())

adjList = [[] for _ in range(N + 1)]
for _ in range(N-1) :
    n1, n2, w = map(int, input().split())
    adjList[n1].append((n2, w))
    adjList[n2].append((n1, w))

for _ in range(M) :
    s, e = map(int, input().split())
    
    que = deque([(s, 0)])
    visited = [False] * (N + 1)
    visited[s] = True

    while que :
        x, d = que.popleft()
        if x == e :
            print(d)
            break

        for adj, w in adjList[x] :
            if visited[adj] :
                continue

            que.append((adj, d + w))
            visited[adj] = True