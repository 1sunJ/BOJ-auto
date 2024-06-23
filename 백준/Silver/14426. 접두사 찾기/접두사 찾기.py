# data / endFlag / children

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = [input().rstrip() for _ in range(N)]

trie = [-1, False, {}]
for s in S :
    p = trie
    for c in s :
        if c not in p[2] :
            p[2][c] = [c, False, {}]
        p = p[2][c]
    p[1] = s

answer = 0
for _ in range(M) :
    s = input().rstrip()

    p = trie
    isPrefix = True
    for c in s :
        if c not in p[2] :
            isPrefix = False
            break
        p = p[2][c]

    if isPrefix :
        answer += 1

print(answer)