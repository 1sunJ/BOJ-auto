def solution(genres, plays):
    l = len(genres)
    hash = {}
    playSums = {}
    
    for i in range(l) :
        genre = genres[i]
        play = plays[i]
        if genre not in hash :
            hash[genre] = [[i, play]]
            playSums[genre] = play
        else :
            hash[genre].append([i, play])
            playSums[genre] += play

    playSumList = []
    for g in playSums :
        playSumList.append((g, playSums[g]))
    playSumList.sort(key=lambda x : x[1], reverse=True)

    for k in hash :
        hash[k].sort(key = lambda x : x[1], reverse=True)

    answer = []
    for g, play in playSumList :
        for i, p in hash[g][:2:] :
            answer.append(i)
    
    return answer

g = ["classic", "pop", "classic", "classic", "pop"]
p = [500, 600, 150, 800, 2500]
print(solution(g, p))
