# 개선 코드

import sys
input = sys.stdin.readline
MAX= sys.maxsize


t = 1
while True :
    N = int(input())
    if N == 0 :
        break

    mtx = [list(map(int, input().split())) for _ in range(N)]

    prev = [MAX, mtx[0][1], mtx[0][1] + mtx[0][2]]

    for i in range(1, N) :
        cur = [0, 0, 0]
        cur[0] = min(prev[0], prev[1]) + mtx[i][0]
        cur[1] = min(prev[0], prev[1], prev[2], cur[0]) + mtx[i][1]
        cur[2] = min(prev[1], prev[2], cur[1]) + mtx[i][2]
        prev = cur

    print("%d. %d" %(t, cur[1]))
    t += 1