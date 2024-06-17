import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize
MOVE = ((-1, 0), (1, 0), (0, -1), (0, 1))

i = 1
while True :
    N = int(input())
    if not N :
        break
    mtx = [list(map(int, input().split())) for _ in range(N)]

    costs = [[INF] * N for _ in range(N)]
    costs[0][0] = mtx[0][0]
    que = []
    heapq.heappush(que, (mtx[0][0], (0, 0)))

    while que :
        w, p = heapq.heappop(que)
        x, y = p

        if x == N-1 and y == N-1 :
            break
        
        for mx, my in MOVE :
            xx, yy = x + mx, y + my
            if not 0 <= xx < N or not 0 <= yy < N :
                continue
                
            if costs[xx][yy] > w + mtx[xx][yy] :
                costs[xx][yy] = w + mtx[xx][yy]
                heapq.heappush(que, (costs[xx][yy], (xx, yy)))

    print("Problem %d: %d" %(i, costs[N-1][N-1]))
    i += 1