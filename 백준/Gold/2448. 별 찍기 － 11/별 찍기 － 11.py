def draw(x, y) :
    mtx[x][y] = '*'
    mtx[x+1][y-1], mtx[x+1][y+1] = '*', '*'
    for i in range(y-2, y+3) :
        mtx[x+2][i] = '*'

def go(x, y, l) :
    if l == 3 :
        draw(x, y)
        return

    ll = l // 2
    go(x, y, ll)
    go(x + ll, y - ll, ll)
    go(x + ll, y + ll, ll)


N = int(input())

mtx = [[' '] * (N*2) for _ in range(N)]

go(0, N-1, N)

for x in mtx :
    print("".join(x))