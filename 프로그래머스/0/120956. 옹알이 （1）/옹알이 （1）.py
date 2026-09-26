s = set(("aya", "ye", "woo", "ma"))

def solution(babbling):
    answer = 0
    for x in babbling :
        idx = 0
        while idx < len(x) :
            if x[idx:idx + 2:] in s :
                idx += 2 
                continue
            if x[idx:idx + 3:] in s :
                idx += 3
            else :
                break
                
        print(x, idx)
        if idx == len(x) :
            answer += 1
    
    return answer