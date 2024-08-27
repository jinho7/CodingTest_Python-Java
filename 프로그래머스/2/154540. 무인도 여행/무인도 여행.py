def dfs(maps, x, y, visited):
    
    # map은 x * y 크기
    rows, cols = len(maps), len(maps[0])
    # stack
    stack = [(x, y)]
    # 방향 벡터
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 총 food
    total_food = 0
    
    # stack이 있을 때 까지
    while stack:
        current_x, current_y = stack.pop()
        # 방문한 적 있으면 Pass
        if visited[current_x][current_y]:
            continue
        
        # 방문한 적 없으면,
        else:
            # 방문했다고 체크 & 총 식량에 추가
            visited[current_x][current_y] = True
            total_food += int(maps[current_x][current_y])

            # 상하좌우 탐색
            for dx, dy in directions:
                next_x, next_y = current_x + dx, current_y + dy
                if (0 <= next_x < rows and 0 <= next_y < cols) and not (visited[next_x][next_y]):
                    if maps[next_x][next_y] != 'X':
                        stack.append((next_x, next_y))
    
    return total_food

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    
    # 모든 칸의 방문 여부를 False로 초기화
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    islands = []
    
    for i in range(rows):
        for j in range(cols):
            if maps[i][j] != 'X' and not visited[i][j]:
                island_days = dfs(maps, i, j, visited)
                islands.append(island_days)
    
    if not islands:
        return [-1]
    
    return sorted(islands)
