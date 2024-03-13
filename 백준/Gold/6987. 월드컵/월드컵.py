GAME_COUNT = 4
TEAM_COUNT = 6

def dfs(i, j) :

    if i == TEAM_COUNT - 1 :
        global isPossible
        isPossible = True
        return
    
    # i 패 무 승
    for x, y in ((0, 2), (1, 1), (2, 0)) :
        if arr[i][x] == 0 or arr[j][y] == 0 :
            continue

        arr[i][x] -= 1
        arr[j][y] -= 1
        if j == TEAM_COUNT - 1 :
            dfs(i+1, i+2)
        else :
            dfs(i, j+1)

        arr[i][x] += 1
        arr[j][y] += 1

for _ in range(GAME_COUNT) :
    input_data = list(map(int, input().split()))
    arr = [[0] * 3 for _ in range(TEAM_COUNT)]
    for i in range(TEAM_COUNT) :
        for j in range(3) :
            arr[i][j] = input_data[i*3 + j]

    isFaultyData = False
    for x in arr :
        if sum(x) != 5 :
            isFaultyData = True
    
    if isFaultyData :
        print(0)
        continue
    
    isPossible = False
    dfs(0, 1)
    print(int(isPossible))