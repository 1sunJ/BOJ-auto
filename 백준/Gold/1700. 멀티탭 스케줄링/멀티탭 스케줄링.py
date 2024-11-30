N, M = map(int, input().split())
arr = list(map(int, input().split()))

s = set() # 멀티탭에 꽂힌 전기 용품

answer = 0
for i in range(M) :
    if len(s) < N or arr[i] in s :
        s.add(arr[i])
        continue

    # 제거할 전기 용품 찾기
    # 현재 멀티탭에 꽂힘 + 가장 가까운 N - 1 개의 전기 용품 찾기
    tmpS = set()
    for j in range(i + 1, M) :
        if arr[j] in s :
            tmpS.add(arr[j])
        if len(tmpS) == N - 1 :
            break

    removeList = list(s - tmpS)
    if removeList :
        s.remove(removeList[0])
    else :
        s.remove(list(s)[0])
    
    answer += 1
    s.add(arr[i])

print(answer)