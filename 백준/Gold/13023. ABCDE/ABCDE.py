import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N)]

for i in range(M) :
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

    # visited, idx(N)
def DFS(visited, idx, n) :
    if n == 5 :
        print(1)
        exit()

    for x in arr[idx] :
        if visited[x] : continue

        visited[x] = True
        DFS(visited, x, n+1)
        visited[x] = False

visited = [False for _ in range(N)]
for i in range(N) :
    visited[i] = True   # 
    DFS(visited, i, 1)
    visited[i] = False

print(0)