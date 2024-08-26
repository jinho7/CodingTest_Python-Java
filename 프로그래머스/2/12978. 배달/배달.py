import heapq
from collections import defaultdict

def solution(N, road, K):
    # 그래프를 인접 리스트 형태로 구성
    graph = defaultdict(list)
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # 다익스트라 알고리즘을 위한 거리 테이블 초기화
    # 노드 1부터 N까지 모든 노드에 대해 거리를 무한대로 초기화
    distances = {node: float('inf') for node in range(1, N + 1)}
    
    # 시작 노드를 1 은 0
    distances[1] = 0

    # 우선순위 큐 (거리, 노드) 튜플을 사용
    priority_queue = [(0, 1)]  # (거리, 노드)
    
    # print(graph)
    
    # 우선순위 큐 있을 때까지
    while priority_queue:
        # 큐에서 가장 짧은 거리의 노드를 꺼냄
        current_distance, current_node = heapq.heappop(priority_queue)

        # 지금 갈려는 게, 저장된 것 보다 긴 경우
        if current_distance > distances[current_node]:
            continue

        # 인접 노드 탐색
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # 더 짧은 경로 발견 시 거리 테이블과 큐를 업데이트
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
            # print(priority_queue)
    # K 이하의 거리인 노드의 수를 계산
    reachable_nodes = sum(1 for distance in distances.values() if distance <= K)
    
    return reachable_nodes
