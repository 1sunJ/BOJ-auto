import sys
input = sys.stdin.readline

N = int(input())
S = [input().rstrip() for _ in range(N)]

# print("======")
trie = [-1, 0, -1, {}]
for s in S :
    p = trie

    found = False
    for c in s :
        if c not in p[3] :
            p[3][c] = [c, 0, -1, {}]
            if not found :
                print(c)
                found = True
        if not found :
            print(c, end = '')
        p = p[3][c]
    p[1] += 1
    p[2] = s
    if p[1] > 1 :
        print(p[1], end = '')
    
    if not found :
        print()