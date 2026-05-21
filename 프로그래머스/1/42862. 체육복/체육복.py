def solution(n, lost, reserve):
    studs = [0] + [1] * n + [0]
    for x in reserve :
        studs[x] = 2
    
    for x in lost :
        studs[x] -= 1

    for i in range(1, n + 1) :
        if studs[i] == 0 :
            if studs[i-1] == 2 :
                studs[i] = 1
                studs[i-1] = 1
            elif studs[i+1] == 2 :
                studs[i] = 1
                studs[i+1] = 1
    
    # print(studs)
    return studs.count(1) + studs.count(2)