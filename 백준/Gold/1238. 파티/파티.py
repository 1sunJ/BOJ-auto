from heapq import *
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(X, d) :
    que = []
    heappush(que, [0, X])

    while que :
        w, cur = heappop(que)

        if w > d[cur] :
            continue

        for ww, v in adjList[cur] :
            ww = ww + w

            if ww < d[v] :
                d[v] = ww
                heappush(que, [ww, v])

N, M, X = map(int, input().split())
X -= 1
adjList = [[] for _ in range(N)]
for _ in range(M) :
    u, v, w = map(int, input().split())
    adjList[u-1].append([w, v-1])

d = [[INF] * N for _ in range(N)]
for i in range(N) :
    d[i][i] = 0
    dijkstra(i, d[i])
    # print(d[i])

answer = 0
for i in range(N) :

    if answer < d[X][i] + d[i][X] :
        answer = d[X][i] + d[i][X]

print(answer)