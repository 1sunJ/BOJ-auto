# data / endFlag / children

import sys
input = sys.stdin.readline

def printTrie(p, depth) :
    print(' ' * depth, end = '')
    if p[0] != -1 :
        print(p[0])

    p[2] = dict(sorted(p[2].items()))
    for x in p[2] :
        printTrie(p[2][x], depth + 1)

N = int(input())
S = [input().rstrip() for _ in range(N)]

trie = [-1, False, {}]
for s in S :
    words = s.split('\\')
    p = trie

    for word in words :
        if word not in p[2] :
            p[2][word] = [word, False, {}]
        p = p[2][word]

printTrie(trie, -1)