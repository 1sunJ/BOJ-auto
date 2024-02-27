import heapq
import sys
input = sys.stdin.readline

def dijkstra(start) :
    que = []
    heapq.heappush(que, [0, start])

    while que :
        w, cur = heapq.heappop(que)

        if w > distance[cur] :
            continue

        for v, ww in adjList[cur] :
            ww = ww + w

            if ww < distance[v] :
                distance[v] = ww
                heapq.heappush(que, [ww, v])

N, M = map(int, input().split())
K = int(input()) - 1
adjList = [[] for _ in range(N)]
for i in range(M) :
    u, v, w = map(int, input().split())
    adjList[u-1].append([v-1, w])

distance = [sys.maxsize] * N
distance[K] = 0

dijkstra(K)

for x in distance : 
    if x == sys.maxsize :
        print("INF")
    else :
        print(x)