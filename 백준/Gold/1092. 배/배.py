N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()

if arr1[-1] < arr2[-1] :
    print(-1)
    exit()

t = 0
while arr2 :
    t += 1

    tmp = []
    for x in arr1[::-1] :
        while arr2 and arr2[-1] > x :
            tmp.append(arr2.pop())
        if arr2 :
            arr2.pop()
    
    arr2 = arr2 + tmp[::-1]

print(t)