import sys

input = sys.stdin.readline
MOVE = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
SCORE = [0, 0, 0, 1, 1, 2, 3, 5, 11]

def dfs(p, x, y, arr) :
    if p[1] == "".join(arr) and p[1] not in find :
        word = p[1]
        find.add(word)
        global score
        global longest
        global cnt

        score += SCORE[len(word)]
        if len(longest) <= len(word) :
            if len(longest) == len(word) :
                longest = min(longest, word)
            else :
                longest = word
        cnt += 1
    
    for mx, my in MOVE :
        mx, my = x + mx, y + my
        if not 0 <= mx < 4 or not 0 <= my < 4 or visited[mx][my] :
            continue

        if mtx[mx][my] in p[2] :
            visited[mx][my] = True
            dfs(p[2][mtx[mx][my]], mx, my, arr + [p[2][mtx[mx][my]][0]])
            visited[mx][my] = False


N = int(input())
words = [input().rstrip() for _ in range(N)]

# value, word(word or False), {}
root = [-1, False, {}]
for word in words : 
    p = root
    for c in word :
        if c not in p[2] :
            p[2][c] = [c, False, {}]
        p = p[2][c]
    p[1] = word

input().rstrip()
T = int(input())
for t in range(T) :
    mtx = [input().rstrip() for _ in range(4)] # 4 * 4
    if t < T - 1 :
        input().rstrip()

    score = 0
    longest = ''
    cnt = 0
    find = set()

    for i in range(4) :
        for j in range(4) :
            if mtx[i][j] not in root[2] :
                continue

            visited = [[False] * 4 for _ in range(4)]
            visited[i][j] = True
            dfs(root[2][mtx[i][j]], i, j, [root[2][mtx[i][j]][0]])

    print(score, longest, cnt)