def dfs(numbers, i, target, result) :
    global answer
    if i == len(numbers) :
        if target == result :
            answer += 1
        return
    
    dfs(numbers, i + 1, target, result + numbers[i])
    dfs(numbers, i + 1, target, result - numbers[i])

def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, 0, target, 0)
    
    return answer