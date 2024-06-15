import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())
adjList = [[] for _ in range(N + 1)]
for _ in range(M) :
    n1, n2, w = map(int, input().split())
    adjList[n1].append((w, n2))
s, e = map(int, input().split())

distance = [INF] * (N + 1)
distance[s] = 0
que = []
heapq.heappush(que, (0, s))

while que :
    w1, n1 = heapq.heappop(que)

    if distance[n1] < w1 :
        continue

    for w2, n2 in adjList[n1] :
        if w1 + w2 < distance[n2] :
            distance[n2] = w1 + w2
            heapq.heappush(que, (w1 + w2, n2))

print(distance[e])