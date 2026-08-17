def dfs(adjList, visited, i) :
    visited[i] = True
    for adj in adjList[i] :
        if not visited[adj] :
            dfs(adjList, visited, adj)
    

def solution(n, computers):
    answer = 0
    adjList = []
    for i in range(n) :
        adj = []
        for j in range(n) :
            if i == j : continue
            if computers[i][j] :
                adj.append(j)
        adjList.append(adj)
    
    visited = [False] * n
    for i in range(n) :
        if not visited[i] :
            answer += 1
            dfs(adjList, visited, i)
    
    return answer