import sys

INF = sys.maxsize
input = sys.stdin.readline

N, M = int(input()), int(input())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1) :
    graph[i][i] = 0

for _ in range(M) :
    v1, v2, w = map(int, input().split())
    graph[v1][v2] = min(w, graph[v1][v2])

for k in range(1, N + 1) :
    for i in range(1, N + 1) :
        for j in range(1, N + 1) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for xx in graph[1::] :
    for x in xx[1::] :
        print(0 if x == INF else x, end = ' ')
    print()