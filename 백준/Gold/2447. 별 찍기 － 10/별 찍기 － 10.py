def makeStars(N) :
    if N == 3 :
        return ['***', '* *', '***']
    
    arr = makeStars(N//3)
    arr2 = []
    for i in arr :
        arr2.append(i*3)
    for i in arr :
        arr2.append(i + ' '*(N//3) + i)
    for i in arr :
        arr2.append(i*3)
    return arr2

print(*makeStars(int(input())), sep='\n')