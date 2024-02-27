X = int(input())

arr = [64]

cnt = 0
while sum(arr) != X :
    cur = arr.pop()
    # print(cur)

    if sum(arr) + cur//2 >= X :
        arr.append(cur//2)
    else :
        arr.append(cur//2)
        arr.append(cur//2)

    # print(arr)

print(len(arr))