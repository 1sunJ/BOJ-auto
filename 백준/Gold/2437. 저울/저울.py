N = int(input())
arr = list(map(int, input().split()))

arr.sort()
if arr[0] != 1 :
    print(1)
    exit()

cnt = 1

for x in arr[1::] :
    if cnt + 1 < x :
        break
    
    cnt += x

print(cnt + 1)