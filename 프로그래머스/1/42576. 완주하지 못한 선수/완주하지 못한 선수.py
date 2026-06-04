def solution(participant, completion):
    part = {}
    for x in participant :
        if x in part :
            part[x] += 1
        else :
            part[x] = 1

    for x in completion :
        part[x] -= 1
        if part[x] == 0 :
            part.pop(x)

    return list(part.keys())[0]