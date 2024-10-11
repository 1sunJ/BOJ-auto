import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
newArr = []

answer = []
p = 0
cur = 1
st = []
while cur <= N :
    if st and arr[p] == st[-1] :
        newArr.append(st.pop())
        p += 1
        answer.append('-')
    else :
        st.append(cur)
        cur += 1
        answer.append('+')

while st :
    newArr.append(st.pop())
    answer.append('-')

if arr == newArr :
    print(*answer, sep = '\n')
else :
    print("NO")