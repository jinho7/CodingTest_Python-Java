# dfs bfs 탐색 기초 다 잡기
def solution(n, computers):
    
    def dfs(cur_node, visited):
        visited.add(cur_node)
        
        for nxt_node in range(n):
            if computers[cur_node][nxt_node] == 1 and nxt_node not in visited:
                dfs(nxt_node, visited)
    
    visited = set()
    answer = 0
    
    for node in range(n):
        if node not in visited:
            dfs(node, visited)
            answer += 1
        
    return answer