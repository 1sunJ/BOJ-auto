import math # up : math.ceil()
import sys
input = sys.stdin.readline

# input : utilize padding
N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# [code 2] :
# calculate number of sections
secN = math.ceil(min(N, M) / 2)
arr2 = [[] for _ in range(secN)]

# arr => arr2
for s in range(secN) :    
    # right
    i = s
    for j in range(s, M-s-1) : arr2[s].append(arr[i][j])
    # down
    j = M-s-1
    for i in range(s, N-s-1) : arr2[s].append(arr[i][j])
    # left
    i = N-s-1
    for j in range(M-s-1, s, -1) : arr2[s].append(arr[i][j])
    # up
    j = s
    for i in range(N-s-1, s, -1) : arr2[s].append(arr[i][j])

# rotate : arr2
for s in range(secN) :
    lenS = len(arr2[s])
    # calculate number of rotation
    newR = R % lenS  # len = ((N+M)*2-8*s-4)
    
    tmp = arr2[s][:newR]
    for i in range(lenS - newR) :
        arr2[s][i] = arr2[s][i+newR]

    for i in range(newR) :
        arr2[s][lenS-newR+i] = tmp[i]

# arr2 => arr
for s in range(secN) :
    idx = 0
    # right
    i = s
    for j in range(s, M-s-1) :
        arr[i][j] = arr2[s][idx]
        idx += 1
    # down
    j = M-s-1
    for i in range(s, N-s-1) :
        arr[i][j] = arr2[s][idx]
        idx += 1
    # left
    i = N-s-1
    for j in range(M-s-1, s, -1) :
        arr[i][j] = arr2[s][idx]
        idx += 1
    # up
    j = s
    for i in range(N-s-1, s, -1) :
        arr[i][j] = arr2[s][idx]
        idx += 1

# output
for x in arr : 
    print(*x)