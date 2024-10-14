def toInt(arr) :
    n = 0
    for x in arr :
        n = 10 * n + x
    return n

N = int(input())
N = sorted(list(map(int, str(N))), reverse=True)

if N[-1] != 0 or sum(N) % 3 != 0:
    print(-1)
    exit()

print(toInt(N))