N = int(input())
arr1 = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
arr2 = [list(map(int, input().split())) for _ in range(M)]

binArr1 = [['b'] + ['0'] * 50 for _ in range(N)]
binArr2 = [['b'] + ['0'] * 50 for _ in range(M)]
for i in range(N) :
    ar = arr1[i]
    for x in ar[1::] :
        binArr1[i][x] = '1'
for i in range(M) :
    ar = arr2[i]
    for x in ar[1::] :
        binArr2[i][x] = '1'

bins1 = []
bins2 = []
for i in range(N) :
    bins1.append("".join(['0'] + binArr1[i]))
for i in range(M) :
    bins2.append("".join(['0'] + binArr2[i]))

answer = [0] * M
for i in range(M) :
    x = bins2[i]
    for y in bins1 :
        if ~int(x, 2) & int(y, 2) > 0 :
            answer[i] += 1

for x in answer :
    print(N - x)