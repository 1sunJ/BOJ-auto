
A = int(input())
B = int(input())

if A == 1 :
    A = 2

arr = [True] * 10001
arr[0] = False
arr[1] = False

for i in range(2, B + 1) :
    if arr[i] :
        for j in range(i * 2, B + 1, i) :
            arr[j] = False

C = 0
D = 0
for i in range(A, B + 1) :
    if arr[i] :
        C += i
        if not D :
            D = i

if not D :
    print(-1)
else :
    print(C)
    print(D)