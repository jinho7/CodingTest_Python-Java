import heapq
from collections import defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    heap = [(0, 1)]
    distances = { i + 1 : float('inf') for i in range(n)}
    distances[1] = 0

    while heap:
        distance, cur_node = heapq.heappop(heap)
        for next_node in graph[cur_node]:
            next_distance = distance + 1
            if next_distance < distances[next_node]:
                distances[next_node] = next_distance
                heapq.heappush(heap, (next_distance, next_node))
                
    target = max(distances.values())
    answer = 0
    for i in distances.values():
        if i == target:
            answer += 1
    return answer