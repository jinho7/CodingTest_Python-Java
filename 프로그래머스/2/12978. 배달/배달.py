import heapq
from collections import defaultdict

def solution(N, road, K):

    graph = defaultdict(list)
    
    for start, end, weight in road:
        graph[start].append((weight, end))
        graph[end].append((weight, start))
        
    print(graph)
    
    # 1부터 각 마을의 최소 거리
    distances = {node : float('inf') for node in range(1, N+1)}
    distances[1] = 0
    
    # 우선순위 큐에 저장 (앞에 기준임 -> (weight, 연결 node) )
    queue = [(0, 1)]
    # heapq.heappush(), heapq.heappop() 으로 함수로만 적으면 힙정렬이 돼서 들어감
    # 선언은 그냥 queue 처럼
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        # 종료 or pass 조건 먼저
        # 만약에 지금 가려는 게 저장된 것 보다 길다면 pass
        if current_distance > distances[current_node]:
            continue
            
        # 해당 노드에서 인접한 노드 모두 탐색
        # 마치 dx, dy in direction 처럼 
        for weight, next_node in graph[current_node]:
            distance = current_distance + weight
            
            # 더 짧은 경로 발견 시 거리 테이블과 큐를 업데이트
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, (distance, next_node))
    
    reachable_nodes = sum(1 for distance in distances.values() if distance <= K)
        
    return reachable_nodes
