import sys
input = sys.stdin.readline

NUMBER_OF_CHARACTER = 26

# input
N, K = map(int, input().split())
strList = [input().rstrip() for _ in range(N)]

K -= 5
if K < 0 :
    print(0)
    exit()

# delete unsufficient letters
for i in range(N) : strList[i] = strList[i][4:len(strList[i])-4:]

# create dictionary : dict[c] = True or False (c = 'a' ~ 'z')
dict = {}
for i in range(NUMBER_OF_CHARACTER) : dict[chr(ord('a') + i)] = False
dict['a'] = True
dict['c'] = True
dict['i'] = True
dict['n'] = True
dict['t'] = True

# make list of character to teach
charToTeach = []
for x in strList : 
    for xx in x :
        if not dict[xx] and not xx in charToTeach :
            charToTeach.append(xx)

if len(charToTeach) <= K :
    print(N)
    exit()

# Backtracking
ans = 0
def ilc(dict, n, idx) : 
    if n == K :
        cnt = 0
        for x in strList :
            ok = True
            for xx in x :
                if not dict[xx] :
                    ok = False
                    break
            if ok : cnt += 1
        
        global ans
        ans = max(ans, cnt)
    
    for i in range(idx + 1, len(charToTeach)) : 
        c = charToTeach[i]
        dict[c] = True
        ilc(dict, n+1, i)
        dict[c] = False


ilc(dict, 0, -1)

print(ans)