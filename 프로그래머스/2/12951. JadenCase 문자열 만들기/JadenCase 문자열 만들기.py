def solution(s):
    arr = s.split()
    
    answer = []
    for x in arr :
        if ord(x[0]) < 65 :
            answer.append(x.lower())
        else :
            answer.append(x[0].upper() + x[1::].lower())
    
    return " ".join(answer)