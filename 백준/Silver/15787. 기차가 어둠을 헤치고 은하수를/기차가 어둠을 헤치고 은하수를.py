import sys
input = sys.stdin.readline

def toDecimal(x) :
    return int(x, 2)

def toBinary(n) :
    return bin(n)

N, M = map(int, input().split())

arr = [1] + [bin(2**20)] * N

for _ in range(M) :
    INPUT = input().rstrip()
    if INPUT.count(' ') == 2 :
        oper, i, x = map(int, INPUT.split())
    else :
        oper, i = map(int, INPUT.split())

    if oper == 1 :
        if arr[i][-x] == '0' :
            n = toDecimal(arr[i]) + 2 ** (x-1)
            arr[i] = toBinary(n)
    elif oper == 2:
        if arr[i][-x] == '1' :
            n = toDecimal(arr[i]) - 2 ** (x-1)
            arr[i] = toBinary(n)
    elif oper == 3:
        n = toDecimal(arr[i])
        if arr[i][-20] == '1' :
            n -= 2 ** 19

        n -= 2 ** 20
        n = (n << 1) + 2 ** 20
        arr[i] = toBinary(n)
    else :
        n = toDecimal(arr[i])
        if arr[i][-1] == '1' :
            n -= 2 ** 0

        n -= 2 ** 20
        n = (n >> 1) + 2 ** 20
        arr[i] = toBinary(n)

answer = set()
for x in arr[1::] :
    answer.add(int(x, 2))

print(len(answer))