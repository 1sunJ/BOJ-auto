def solution(number, k):
    arr = []
    i = 0
    while k > 0 and i < len(number) :
        if not arr or arr[-1] >= number[i] :
            arr.append(number[i])
            i += 1
        else :
            arr.pop()
            k -= 1

    arr += list(number[i::])
    
    if k > 0 :
        arr = arr[:-k:]

    return ''.join(arr)