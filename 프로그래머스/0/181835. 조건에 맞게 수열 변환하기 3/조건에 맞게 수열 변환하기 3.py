def solution(arr, k):
    for i in range(len(arr)) :
        arr[i] = arr[i] * k if k % 2 else arr[i] + k
        
    return arr