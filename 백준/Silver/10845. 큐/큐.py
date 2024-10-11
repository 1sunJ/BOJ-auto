from collections import deque

import sys
input = sys.stdin.readline

que = []
for _ in range(int(input())) :
    oper = input().rstrip()

    if oper[:4] == 'push' :
        n = int(oper[5::])
        que.append(n)
    elif oper[:3] == 'pop' :
        if not que :
            print(-1)
        else :
            print(que.pop(0))
    elif oper[:4] == 'size' :
        print(len(que))
    elif oper[:5] == 'empty' :
        print(int(not que))
    elif oper[:5] == 'front' :
        if not que :
            print(-1)
        else :
            print(que[0])
    elif oper[:4] == 'back' :
        if not que :
            print(-1)
        else :
            print(que[-1])