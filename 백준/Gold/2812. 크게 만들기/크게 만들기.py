N, K = map(int, input().split())
arr = list(map(int, input()))

# st = [arr[0]]
st = [0]
s = set()
removeArr = []

for i in range(1, N) :
    while st and arr[st[-1]] < arr[i] : 
        # removeArr.append(st.pop())
        s.add(st.pop())
        if len(s) == K :
            break

    # st.append(arr[i])
    st.append(i)

    if len(s) == K :
        break

for i in range(N-1, -1, -1) :
    if len(s) == K :
        break

    if not i in s :
        s.add(i)

# print(removeArr)
# print(s)

for i in range(N) :
    if not i in s :
        print(arr[i], end = '')