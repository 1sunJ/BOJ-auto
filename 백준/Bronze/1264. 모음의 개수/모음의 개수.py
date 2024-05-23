AEIOU = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')

while True :
    s = input()
    if s == '#' :
        break
    
    answer = 0
    for c in s :
        if c in AEIOU :
            answer += 1
    
    print(answer)