
def recur(depth, part) :
    # print("!!", depth, part)
    global isFound
    if isFound is not None:
        return

    # 분리
    part1 = part # part[0] | part[0] + size[depth - 1]
    part2 = part1 + sizes[depth - 1] # part1 | part1 + depth + 3
    part3 = part2 + depth + 3
    # print(part1, part2, part3)


    # 베이스 케이스
    if N in(part1, part2, part3) :
        isFound = 'm'
        return

    if depth == 0 :
        isFound = 'o'
        return
    
    # 재귀
    if N < part2 :        
        recur(depth - 1, part1)
    elif part2 <= N < part3 :
        isFound = 'o'
        return
    else :
        recur(depth - 1, part3)

N = int(input())

# make size list
sizes = [3]
k = 1
while sizes[-1] <= 10 ** 9 :
    sizes.append(sizes[-1] * 2 + (k + 3))
    k += 1

# find depth
depth = 0
while N >= sizes[depth] :
    depth += 1

# recur
isFound = None
recur(depth, 1)
print(isFound)