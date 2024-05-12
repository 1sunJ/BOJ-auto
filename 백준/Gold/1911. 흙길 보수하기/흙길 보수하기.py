import math

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key = lambda x : x[0])
for i in range(N) :
    arr[i][1] -= 1

last = -1
answer = 0
for s, e in arr :
    if e < last :
        continue
    elif last < s :
        answer += math.ceil((e-s+1) / L)
        last = s + math.ceil((e-s+1) / L) * L
    else : # s <= last <= e
        answer += math.ceil((e-last+1) / L)
        last = last + math.ceil((e-last+1) / L) * L

print(answer)