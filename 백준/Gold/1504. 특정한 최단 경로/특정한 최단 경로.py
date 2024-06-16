import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(s) :
    distance = [INF] * (N + 1) # 노드 s에서 각 노드로 가는 비용 리스트
    distance[s] = 0
    que = []
    heapq.heappush(que, (0, s))

    while que :
        w1, v1 = heapq.heappop(que)

        if distance[v1] < w1 :
            continue

        for w2, v2 in adjList[v1] :
            if w1 + w2 < distance[v2] :
                distance[v2] = w1 + w2
                heapq.heappush(que, (w1 + w2, v2))

    return distance

N, M = map(int, input().split())
adjList = [[] for _ in range(N + 1)]
for _ in range(M) :
    v1, v2, w = map(int, input().split()) # 출발지, 도착지, 비용
    adjList[v1].append((w, v2))
    adjList[v2].append((w, v1))
u, v = map(int, input().split())

distance1 = dijkstra(1)
distanceU = dijkstra(u)
distanceV = dijkstra(v)

result1 = distance1[u] + distanceU[v] + distanceV[N]
result2 = distance1[v] + distanceV[u] + distanceU[N]

answer = min(result1, result2)
print(answer if answer < INF else -1)