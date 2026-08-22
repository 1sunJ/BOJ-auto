def solution(num_list):
    a, b = 1, 0
    
    for x in num_list :
        a *= x
        b += x
    b **= 2
    
    return 1 if a < b else 0