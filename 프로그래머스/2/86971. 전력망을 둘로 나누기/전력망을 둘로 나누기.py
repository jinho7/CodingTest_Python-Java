from collections import defaultdict
import math

def solution(n, wires):
    def find_all_nodes(wires, canceled_edge):
        a, b = canceled_edge
        
        edge_dict = defaultdict(list)
        
        for x, y in wires:
            if (x, y) == (a, b):
                continue
            edge_dict[x].append(y)
            edge_dict[y].append(x)

        def dfs(x):
            cnt = 1
            for i in edge_dict[x]:
                if i not in visited:
                    visited.add(i)
                    cnt += dfs(i)
            return cnt
        
        
        visited = set()
        visited.add(a)
        count_a = dfs(a)

        visited = set()
        visited.add(b)
        count_b = dfs(b)

        return abs(count_a - count_b)
    
    answer = n
    for i in range(len(wires)):
        nodes_abs = find_all_nodes(wires, wires[i])
        if nodes_abs < answer:
            answer = nodes_abs
    return answer