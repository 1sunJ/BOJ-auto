T = int(input())
N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

cumArr1 = arr1[::] + [0]
cumArr2 = arr2[::] + [0]

for i in range(1, N) :
    cumArr1[i] += cumArr1[i-1]

for i in range(1, M) :
    cumArr2[i] += cumArr2[i-1]

sums = dict()
for i in range(M) :
    for j in range(i, M) :
        x = cumArr2[j] - cumArr2[i-1]
        if x in sums :
            sums[x] += 1
        else :
            sums[x] = 1

answer = 0
for i in range(N) :
    for j in range(i, N) :
        x = cumArr1[j] - cumArr1[i-1]
        if T - x in sums :
            answer += sums[T - x]

print(answer)