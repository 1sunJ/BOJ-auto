import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

for _ in range(int(input())) :
    N = int(input())
    
    parentList = [0] * (N+1)
    for i in range(N-1) :
        a, b = map(int, input().split())
        parentList[b] = a

    a, b = map(int, input().split())
    aParent = [a]
    bParent = [b]
    
    now = a
    while parentList[now] :
        aParent.append(parentList[now])
        now = parentList[now]

    now = b
    while parentList[now] :
        bParent.append(parentList[now])
        now = parentList[now]

    # print(aParent)
    # print(bParent)

    answer = aParent[-1]
    while aParent and bParent and aParent[-1] == bParent[-1] :
        answer = aParent[-1]
        aParent.pop()
        bParent.pop()

    print(answer)