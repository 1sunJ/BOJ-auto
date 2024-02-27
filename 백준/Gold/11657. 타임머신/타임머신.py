import sys
input = sys.stdin.readline

START = 1
INF = sys.maxsize

def bellman_ford(start) :
    d[START] = 0

    for i in range(N) :
        for cur, next, wage in edges :
            if d[cur] != INF and d[next] > d[cur] + wage :
                d[next] = d[cur] + wage

                if i == N - 1 :
                    return True
                
    return False

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

d = [INF] * (N+1)

negative_cycle = bellman_ford(START)

if negative_cycle :
    print(-1)
else :
    for x in d[2::] :
        if x == INF :
            print(-1)
        else :
            print(x)