from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

adjList = [[] for _ in range(N)]
for i, j in arr :
    adjList[i-1].append(j-1)
    adjList[j-1].append(i-1)

# for x in adjList :
#     x.sort()

visited = [-1] * N
visited[0] = 0
que = deque([0])

while que :
    p = que.popleft()

    for x in adjList[p] :
        if visited[x] == -1 :
            visited[x] = visited[p] + 1
            que.append(x)

answer2 = max(visited)
answer3 = visited.count(answer2)
for i in range(N) :
    if answer2 == visited[i] :
        answer1 = i
        break

print(answer1+1, answer2, answer3)