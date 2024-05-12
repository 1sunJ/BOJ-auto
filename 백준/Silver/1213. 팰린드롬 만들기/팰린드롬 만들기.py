SORRY = "I'm Sorry Hansoo"

arr = list(input())
arr.sort()

result = []

special = False
while arr :
    if len(arr) == 1 :
        if special :
            result = SORRY
        else :
            special = arr[0]
        break

    if arr[0] == arr[1] :
        result.append(arr[0])
        del arr[0]
        del arr[0]
    else :
        if special :
            result = SORRY
            break
        else :
            special = arr[0]
            del arr[0]

if result == SORRY :
    print(result)
else :
    print(*result, sep = '', end = '')
    if special :
        print(special, sep = '', end = '')
    print(*result[::-1], sep = '')