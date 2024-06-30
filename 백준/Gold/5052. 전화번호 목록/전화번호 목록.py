import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    N = int(input())
    arr = [input().rstrip() for _ in range(N)]

    arr.sort()

    answer = "YES"
    for i in range(N-1) :
        if arr[i] == arr[i+1][:len(arr[i])] :
            answer = "NO"
            break

    print(answer)