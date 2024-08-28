from collections import deque

def bfs(start_x, start_y, maps, target):
    rows = len(maps)
    cols = len(maps[0])
    
    # 방문 여부를 기록할 배열
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS를 위한 큐 초기화
    queue = deque([(start_x, start_y, 0)])  # (x, y, 거리)
    visited[start_x][start_y] = True
    
    while queue:
        x, y, distance = queue.popleft()
        
        # 목표 지점에 도달한 경우
        if maps[x][y] == target:
            return distance
        
        # 네 방향으로 이동
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            
            # 범위를 벗어나지 않고, 방문하지 않았으며, 벽이 아닌 경우
            if 0 <= next_x < rows and 0 <= next_y < cols and not visited[next_x][next_y] and maps[next_x][next_y] != 'X':
                visited[next_x][next_y] = True
                queue.append((next_x, next_y, distance + 1))
    
    # 목표 지점에 도달할 수 없는 경우
    return -1

def solution(maps):
    # 시작점, 레버, 출구 위치 찾기
    start_x, start_y = None, None
    lever_x, lever_y = None, None
    exit_x, exit_y = None, None
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start_x, start_y = i, j
            elif maps[i][j] == 'L':
                lever_x, lever_y = i, j
            elif maps[i][j] == 'E':
                exit_x, exit_y = i, j
    
    # 시작점에서 레버까지의 최단 거리
    distance_to_lever = bfs(start_x, start_y, maps, 'L')
    if distance_to_lever == -1:
        return -1
    
    # 레버에서 출구까지의 최단 거리
    distance_to_exit = bfs(lever_x, lever_y, maps, 'E')
    if distance_to_exit == -1:
        return -1
    
    # 총 이동 거리
    return distance_to_lever + distance_to_exit

