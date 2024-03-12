def printExpression(arr) :
    # print("arr", arr)
    for x in arr :
        if list(map(int, str(abs(x))))[0] == 1 :
            pass
        elif x >= 0 :
            print('+', end = '')
        else :
            print('-', end = '')

        if abs(x) < 10 :
            print(abs(x), end = '')
        else :
            n = list(map(int, str(abs(x))))
            print(*n, sep = ' ', end = '')

    print()

def dfs(i, arr) :
    if i == N :
        if sum(arr) == 0 :
            printExpression(arr)
        return

    # 1. 공백
    tmp = arr[::]
    i += 1
    last = tmp.pop()
    if last > 0 :
        dfs(i, tmp + [last*10 + i])
    else :
        dfs(i, tmp + [-(-last*10 + i)])

    # 2. +
    dfs(i, arr + [i])
    
    # 3. -
    dfs(i, arr + [-i])


for _ in range(int(input())) :
    N = int(input())
    dfs(1, [1])
    print()