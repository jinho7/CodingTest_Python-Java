def solution(grid):
    # 격자의 크기
    rows, cols = len(grid), len(grid[0])
    
    # 방문 기록
    visited = [[[False] * 4 for _ in range(cols)] for _ in range(rows)]
    
    # 이동 방향: 상(0), 우(1), 하(2), 좌(3)
    direction_moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # 빛이 이동하면서 좌회전(L), 우회전(R)을 반영한 방향 변화
    def turn_left(d): return (d - 1) % 4
    def turn_right(d): return (d + 1) % 4

    # DFS 탐색을 위한 함수
    def dfs(x, y, direction):
        length = 0
        # 사이클 탐색 시작
        while not visited[x][y][direction]:
            # 방문 기록
            visited[x][y][direction] = True
            # 사이클 길이 + 1
            length += 1
            
            # 다음 방향 결정
            if grid[x][y] == 'L':
                direction = turn_left(direction)
            elif grid[x][y] == 'R':
                direction = turn_right(direction)

            # 현재 방향으로 이동 (반대방향으로 이동되는 것을 모듈러 연산으로 처리)
            x = (x + direction_moves[direction][0]) % rows
            y = (y + direction_moves[direction][1]) % cols
        
        return length

    result = []

    # 각 좌표마다 4개의 방향을 체크하며 사이클을 탐색
    for i in range(rows):
        for j in range(cols):
            # 상하좌우 = 0123
            for d in range(4):
                # 해당 좌표와 방향을 방문한 적이 없다면
                if not visited[i][j][d]:
                    # DFS 호출
                    cycle_length = dfs(i, j, d)
                    if cycle_length > 0:
                        result.append(cycle_length)

    # 사이클 길이를 오름차순 정렬 후 반환
    return sorted(result)