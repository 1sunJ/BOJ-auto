def check(i1, j1, l) :
    for i in range(i1, i1 + l) :
        for j in range(j1, j1 + l) :
            if mtx[i1][j1] != mtx[i][j] :
                return False
            
    return True

def sep(i, j, l) :
    if check(i, j, l) :
        result[mtx[i][j]] += 1
    else :
        for ii in range(i, i + l, l // 3) :
            for jj in range(j, j + l, l // 3) :
                sep(ii, jj, l // 3)

N = int(input())
mtx = [list(map(int, input().split())) for _ in range(N)]

result = [0] * 3
sep(0, 0, N)

print(result[-1])
print(result[0])
print(result[1])