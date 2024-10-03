def solution(grid):
    # 격자의 크기
    rows, cols = len(grid), len(grid[0])
    
    # 방문 기록
    # 3차원 내부는 상, 우, 하, 좌
    visited = [[[False] * 4 for _ in range(cols)] for _ in range(rows)]
    
    # 이동 방향: 상(0), 우(1), 하(2), 좌(3)
    # 시계 방향으로 지정
    direction_moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # 빛이 이동하면서 좌회전(L), 우회전(R)을 반영한 방향 변화
    def turn_left(d): return (d - 1) % 4
    def turn_right(d): return (d + 1) % 4
    
    result = []

    # 각 좌표마다 4개의 방향을 체크하며 사이클을 탐색
    for i in range(rows):
        for j in range(cols):
            # 상하좌우 = 0123
            for d in range(4):
                # 해당 좌표와 방향을 방문한 적이 없다면
                if not visited[i][j][d]:
                    # 초기화
                    length = 0
                    x, y, direction = i, j, d
                    
                    # 사이클 탐색 시작
                    while not visited[x][y][direction]:
                        # 방문 기록
                        visited[x][y][direction] = True
                        # 사이클 길이 + 1
                        length += 1
                        
                        # 다음 좌표로 이동
                        if grid[x][y] == 'L':
                            direction = turn_left(direction)
                        elif grid[x][y] == 'R':
                            direction = turn_right(direction)
                        
                        # 현재 방향으로 이동
                        x = (x + direction_moves[direction][0]) % rows
                        y = (y + direction_moves[direction][1]) % cols
                    
                    # 사이클이 완성된 경우 길이를 저장
                    result.append(length)

    # 사이클 길이를 오름차순 정렬 후 반환
    return sorted(result)
