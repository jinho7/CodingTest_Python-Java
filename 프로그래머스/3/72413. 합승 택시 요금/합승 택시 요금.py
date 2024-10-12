import heapq
from collections import defaultdict

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    
    for start, end, weight in fares:
        graph[start].append((weight, end))
        graph[end].append((weight, start))
        
    def distances_bfs(from_node):
        distances = { node : float('inf') for node in range(1, n+1) }

        # 시작 지점 거리 체크
        distances[from_node] = 0
        # 우선순위 큐에 저장 (앞에 기준임 -> (weight, 연결 node) )
        queue = [(0, from_node)]

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            for weight, next_node in graph[current_node]:
                distance = current_distance + weight

                # 더 짧은 경로 발견 시 거리 테이블과 큐를 업데이트
                if distance < distances[next_node]:
                    distances[next_node] = distance
                    heapq.heappush(queue, (distance, next_node))
        
        return distances
    
    s_distances = distances_bfs(s)
    a_distances = distances_bfs(a)
    b_distances = distances_bfs(b)
    
    print(s_distances)
    print(a_distances)
    print(b_distances)
    
    min_distance = float('inf')
    for target in range(1, n+1):
        sum_distance = s_distances[target] + a_distances[target] + b_distances[target]
        if sum_distance < min_distance:
            min_distance = sum_distance
            
    return min_distance