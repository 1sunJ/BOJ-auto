N = int(input())
arr = list(map(int, input().split()))

st = [0]
ngeArr = [False] * N

for i in range(1, N) :
    while st and arr[st[-1]] < arr[i] :
        ngeArr[st.pop()] = arr[i]

    st.append(i)

while st :
    ngeArr[st.pop()] = -1

print(*ngeArr)