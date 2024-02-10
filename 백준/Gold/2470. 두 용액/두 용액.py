N = int(input())
arr = list(map(int, input().split()))

arr.sort()
l, r = 0, N-1

answer1 = abs(arr[l] + arr[r])
answer2 = [l, r]

while l < r :
    # print("l r", l, r)

    summ = arr[l] + arr[r]
    
    if answer1 > abs(summ) :
        answer1 = abs(summ)
        answer2 = [l, r]

    if summ > 0 :
        r -= 1
    elif summ < 0 :
        l += 1
    else :
        break

# print(answer1)
l, r = answer2
print(arr[l], arr[r])