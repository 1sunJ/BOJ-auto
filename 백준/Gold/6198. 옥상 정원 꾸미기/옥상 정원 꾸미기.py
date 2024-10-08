N = int(input())
arr = [int(input()) for _ in range(N)]

st = [0]

answer = 0
for i in range(1, N) :
    while st and arr[st[-1]] <= arr[i] :
        answer += i - st.pop() - 1
    st.append(i)

while st :
    answer += N - st.pop() - 1

print(answer)