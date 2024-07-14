import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N, M, K = map(int, input().split())

adjList = [[] for _ in range(N + 1)]
for _ in range(M) :
    u, v, t = map(int, input().split())
    adjList[u].append([v, t])
    adjList[v].append([u, t])

distance = [[INF] * (K + 1) for _ in range(N + 1)]
for k in range(K + 1) :
    distance[1][k] = 0

que = []
heapq.heappush(que, (0, 1, 0)) # weight, node, p

while que :
    w, v, p = heapq.heappop(que)

    if distance[v][p] < w :
        continue

    if p + 1 <= K :
        for u, w2 in adjList[v] :
            if distance[u][p + 1] > w :
                distance[u][p + 1] = w
                heapq.heappush(que, (w, u, p + 1))

    for u, w2 in adjList[v] :
        if distance[u][p] > w + w2 :
            distance[u][p] = w + w2
            heapq.heappush(que, (w + w2, u, p))

print(min(distance[-1]))