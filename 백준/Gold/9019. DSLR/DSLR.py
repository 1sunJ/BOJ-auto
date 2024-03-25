import sys
from collections import deque
input = sys.stdin.readline
c = ['D', 'S', 'L', 'R']

def CalD(n) :
    return (2 * n) % 10000

def CalS(n) :
    if n > 0 :
        return n - 1
    else :
        return 9999

def CalL(n) :
    if n >= 1000 :
        return (n % 1000) * 10 + n // 1000
    else :
        return n * 10

def CalR(n) :
    return (n % 10) * 1000 + n // 10

for _ in range(int(input())) :
    A, B = map(int, input().split())

    visited = [False] * 10000
    que = deque([])
    visited[A] = True
    que.append([A, []])

    while que :
        x, operList = que.popleft()
        if x == B :
            print(*operList, sep = '')
            break

        y = [CalD(x), CalS(x), CalL(x), CalR(x)]
        for i in range(4) :
            if not visited[y[i]] :
                que.append([y[i], operList + [c[i]]])
                visited[y[i]] = True