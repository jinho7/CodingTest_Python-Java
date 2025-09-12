from collections import defaultdict
import math

def solution(n, wires):
    
    edge_dict = defaultdict(list)
    for x, y in wires:
        edge_dict[x].append(y)
        edge_dict[y].append(x)

    def dfs(u, visited):
        cnt = 1
        for v in edge_dict[u]:
            if v not in visited:
                visited.add(v)
                cnt += dfs(v, visited)
        return cnt

    answer = n
    for x, y in wires:
        visited = {x, y}
        answer = min(abs(n - 2 * dfs(x, visited)), answer)
    return answer