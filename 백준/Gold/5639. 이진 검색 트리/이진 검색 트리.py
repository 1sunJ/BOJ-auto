import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def postorder(start, end) :
    if start > end :
        return
    
    mid = end + 1
    for i in range(start + 1, end + 1) :
        if arr[start] <= arr[i] :
            mid = i
            break

    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(arr[start])
    

arr = []
while True :
    try :
        x = int(input())
        arr.append(x)
    except :
        break

postorder(0, len(arr) - 1)