from collections import deque
import sys
input = sys.stdin.readline

# parameter : 두 치킨집 건물 
# return : 모든 도시에서의 왕복 시간의 합
def bfs(b1, b2) :

    que = deque([b1]) 
    visited1 = [False] * N
    visited1[b1] = 1

    while que :
        x = que.popleft()

        for i in idjList[x] : 
            if visited1[i] : 
                continue

            visited1[i] = visited1[x] + 1
            que.append(i)

    que = deque([b2])
    visited2 = [False] * N
    visited2[b2] = 1

    while que :
        x = que.popleft()

        for i in idjList[x] : 
            if visited2[i] : 
                continue

            visited2[i] = visited2[x] + 1
            que.append(i)

    result = 0
    for i in range(N) :
        result += (min(visited1[i], visited2[i]) - 1) * 2

    return result
    

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

idjList = [[] for _ in range(N)] # 인접 리스트
for i in range(M) :
    idjList[arr[i][0] - 1].append(arr[i][1] - 1)
    idjList[arr[i][1] - 1].append(arr[i][0] - 1)

answer1 = 0, 1
answer2 = sys.maxsize
for i in range(N-1) :
    for j in range(i+1, N) :
        # print("!!!!", i+1, j+1)
        result = bfs(i, j)
        if answer2 > result :
            answer1 = (i+1, j+1)
            answer2 = result
        answer2 = min(answer2, bfs(i, j))

print(*answer1, answer2)