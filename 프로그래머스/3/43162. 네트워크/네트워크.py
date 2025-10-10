from collections import deque

# dfs bfs 탐색 기초 다 잡기
def solution(n, computers):
    
    visited = set()
    answer = 0

    for node in range(n):
        if node not in visited:
            q = deque([node])
            while q:
                cur_node = q.popleft()
                visited.add(cur_node)

                for nxt_node in range(n):
                    if computers[cur_node][nxt_node] == 1 and nxt_node not in visited:
                        q.append(nxt_node)
            answer += 1
    return answer