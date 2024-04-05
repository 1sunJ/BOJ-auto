import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(i) :
    for adj, w in adjList[i] :
        if visited[adj] != -1 :
            continue

        visited[adj] = visited[i] + w
        dfs(adj)

N = int(input())
adjList = [[] for _ in range(N+1)]
for _ in range(N-1) :
    u, v, w = map(int, input().split())
    adjList[u].append((v, w))
    adjList[v].append((u, w))

visited = [-1] * (N+1)
visited[1] = 0
dfs(1)
# print(visited)

maxValue = 0
maxIdx = 1
for i in range(2, N+1) :
    if maxValue < visited[i] :
        maxValue = visited[i]
        maxIdx = i

visited = [-1] * (N+1)
visited[maxIdx] = 0
dfs(maxIdx)
# print(maxIdx, visited)

print(max(visited))