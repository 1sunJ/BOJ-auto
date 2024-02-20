for _ in range(int(input())) :
    w = input().rstrip()
    K = int(input())
    l = len(w)

    d = {}
    for i in range(ord('a'), ord('z') + 1) :
        d[chr(i)] = []

    for i in range(l) :
        d[w[i]].append(i)

    s = set()
    for i in range(ord('a'), ord('z') + 1) :
        if len(d[chr(i)]) >= K :
            s.add(chr(i))

    # print(d)
    # print(s)

    # find answer
    answer1 = l
    answer2 = 0
    
    for x in s :
        for i in range(len(d[x]) - K + 1) :
            answer1 = min(answer1, d[x][i+K-1] - d[x][i] + 1)
            answer2 = max(answer2, d[x][i+K-1] - d[x][i] + 1)

    if answer2 :
        print(answer1, answer2)
    else :
        print(-1)