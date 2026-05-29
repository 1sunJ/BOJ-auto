def solution(participant, completion):
    hash = {}
    for x in participant:
        if x in hash:
            hash[x] += 1 
        else :
            hash[x] = 1 
    hash2 = {}  
    for x in completion:
         if x in hash2:
             hash2[x] += 1
         else:
             hash2[x] = 1

    for x in hash2:
        hash[x] -= hash2[x]
        
        if hash[x] == 0:
            del hash[x]

    return list(hash.keys())[0]

   