def remake() :
    global arr

    tmp1 = []
    tmp2 = []
    for i in range(len(arr)) :
        if i % 2 :
            tmp2.append(arr[i])
        else :
            tmp1.append(arr[i])

    arr = tmp1[::] + tmp2[::-1]

def findCycle(X) :

    for i in range(1, X+1) :
        remake()
        strList.append(arr[::])

        if arr == origin :
            return i
    
    print(*arr, sep = '')
    exit()

X = int(input())
arr = list(input())

origin = arr[::]
strList = [arr[::]]

cycle = findCycle(X)
print(*strList[X % cycle], sep = '')