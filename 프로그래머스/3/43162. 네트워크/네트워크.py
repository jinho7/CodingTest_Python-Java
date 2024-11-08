def solution(n, computers):
    visited = [False] * n
    count = 0
    
    def dfs(node):
        visited[node] = True
        for next_node in range(n):
            if computers[node][next_node] == 1 and not visited[next_node]:
                dfs(next_node)
                
    for node in range(n):
        if not visited[node]:
            dfs(node)
            count += 1  # 새로운 그래프 발견
            
    return count