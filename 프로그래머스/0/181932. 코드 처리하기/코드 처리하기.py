def solution(code):
    answer = ''
    
    mode = 0
    for i in range(len(code)) :
        x = code[i]
        
        if x == "1" :
            mode = 1 if mode == 0 else 0
            continue
        
        if mode == 0 and i % 2 == 0 :
            answer += x
        
        if mode == 1 and i % 2 == 1 :
            answer += x
            
    if not answer :
        answer = "EMPTY"
        
    return answer