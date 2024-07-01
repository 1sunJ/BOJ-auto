import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

st = []
size = 0
answer = 0

for x in arr :
    if size == 0 :
        st.append([x, 1])
        size += 1
        continue

    cnt = 0
    while size > 0 and st[-1][0] < x :
        cnt += st[-1][1]
        size -= st[-1][1]
        st.pop()

    if size > 0 :
        if st[-1][0] != x :
            cnt += 1
        else :
            cnt += st[-1][1]
            if len(st) >= 2 :
                cnt += 1
    
    answer += cnt

    if size > 0 and st[-1][0] == x :
        st[-1][1] += 1
    else :
        st.append([x, 1])
    size += 1

print(answer)