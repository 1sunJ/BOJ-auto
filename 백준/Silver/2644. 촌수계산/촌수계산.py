from collections import deque

N = int(input())
s, e = map(int, input().split())
M = int(input())

adjList = [[] for _ in range(N + 1)]
for _ in range(M) :
    x, y = map(int, input().split())
    adjList[x].append(y)
    adjList[y].append(x)

que = deque([(s, 0)])
visited = [False] * (N + 1)
visited[s] = True

while que :
    p, depth = que.popleft()

    if p == e :
        print(depth)
        exit()

    for next in adjList[p] :
        if visited[next] :
            continue

        visited[next] = True
        que.append((next, depth + 1))
    
print(-1)