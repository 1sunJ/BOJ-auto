from collections import deque
import sys
input = sys.stdin.readline
maxS = 100001

# input
N, K = map(int, input().split())

# BFS
que = deque([N])
visited = [0] * maxS
visited[N] = 1

while que :
    x = que.popleft()

    if x == K :
        break

    # ★★ insert into queue before x-1, x+1
    if x*2 < maxS and not visited[x*2] :
        que.append(x*2)
        visited[x*2] = visited[x]
   
    if x-1 >= 0 and not visited[x-1] :
        que.append(x-1)
        visited[x-1] = visited[x] + 1

    if x+1 < maxS and not visited[x+1] :
        que.append(x+1)
        visited[x+1] = visited[x] + 1

# output
print(visited[K]-1)