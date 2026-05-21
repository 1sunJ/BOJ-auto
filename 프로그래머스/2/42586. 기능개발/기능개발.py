from collections import deque

def solution(progresses, speeds):
    deq = deque([])
    for i in range(len(progresses)) :
        deq.append((progresses[i], speeds[i]))


    answer = []
    while deq :
        p, s = deq.popleft()
        print(p, s)
        days = (100 - p + s - 1) // s
        # print("in while", p, days)

        cnt = 1
        for pp, ss in deq :
            newDays = (100 - pp + ss - 1) // ss
            # print("in for", pp, ss, newDays)
            if days >= newDays :
                cnt += 1
            else :
                break
        
        for i in range(cnt - 1) :
            deq.popleft()

        answer.append(cnt)

    return answer