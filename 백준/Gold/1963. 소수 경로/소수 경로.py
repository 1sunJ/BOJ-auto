import sys
from collections import deque

input = sys.stdin.readline

def makeNew(N, idx, n) :
    tmp = list(map(int, str(N)))

    tmp[idx] = n

    new = 0
    for x in tmp :
        new *= 10
        new += x

    return new

primes = [False, False] + [True] * 9999
for i in range(2, 10001) :
    if not primes[i] :
        continue

    for j in range(i * 2, 10001, i) :
        primes[j] = False

for _ in range(int(input())) :
    s, e = map(int, input().split())

    que = deque([(s, 0)])
    visited = [False] * 10001
    visited[s] = True

    isFound = False
    while que :
        x, t = que.popleft()

        if x == e :
            print(t)
            isFound = True
            break

        for idx in range(4) :
            for i in range(0, 10) :
                next = makeNew(x, idx, i)
                if next < 1000 :
                    continue

                if visited[next] or not primes[next] :
                    continue

                visited[next] = True
                que.append((next, t + 1))

    if not isFound :
        print("impossible")