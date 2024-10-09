import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())) :
    n = int(input())
    sx, sy = map(int, input().split())
    cons = [list(map(int, input().split())) for _ in range(n)]
    ex, ey = map(int, input().split())

    que = deque([(sx, sy)])
    visited = [False] * n

    result = False
    while que :
        sxx, syy = que.popleft()
        
        if abs(sxx - ex) + abs(syy - ey) <= 1000 :
            result = True
            break

        for i in range(n) :
            cx, cy = cons[i]
            if abs(cx - sxx) + abs(cy - syy) > 1000 or visited[i] :
                continue

            visited[i] = True
            que.append((cx, cy))

    print("happy" if result else "sad")